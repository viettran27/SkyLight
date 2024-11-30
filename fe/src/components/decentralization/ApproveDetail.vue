<script setup>
import { computed } from 'vue';

import { axiosClient } from '@/lib/axios';
import { isApprove, statusFit } from '@/utils';
import { STATUS_APPROVE } from '@/constants';

import { Search } from 'lucide-vue-next';
import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

const { user, id_pr, details } = defineProps({
  user: Object,
  id_pr: String, 
  details: Array
})
const emits = defineEmits(['getData', 'handleSearch']);

const handleApprove = () => {
	const data = {
		Status: STATUS_APPROVE.APPROVED,
		Ma_PR: id_pr,
		Auth: user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		emits('getData');
	});
};

const handleReject = () => {
	const data = {
		Status: STATUS_APPROVE.REJECTED,
		Ma_PR: id_pr,
		Auth: user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		emits('getData');
	});
};

const canApprove = computed(() => {
	const status = statusFit(user?.skylight);
	return details?.[0]?.['Trang_thai'] === status;
});
</script>

<template>
	<div class="flex justify-between item-center bg-white px-3 py-5">
		<div class="relative w-full max-w-[250px] items-center">
			<Input
				id="search"
				type="text"
				@input="$emit('handleSearch', $event.target.value)"
				placeholder="Nhập mã vật liệu"
				class="pl-10"
			/>
			<span
				class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
			>
				<Search class="size-6 text-muted-foreground" />
			</span>
		</div>
		<div
			v-if="isApprove(user?.skylight) && canApprove"
			class="flex items-center gap-2"
		>
			<Button variant="destructive" @click="handleReject"
				>Không duyệt</Button
			>
			<Button @click="handleApprove">Duyệt</Button>
		</div>
	</div>
</template>
