<script setup>
import { computed } from 'vue';

import { axiosClient } from '@/lib/axios';
import { isApprove, statusFit } from '@/utils';
import { STATUS_APPROVE } from '@/constants';

import { Search, Plus } from 'lucide-vue-next';
import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

const { user, status, id_pr } = defineProps({
	user: Object,
	status: String,
	id_pr: String,
});
const emit = defineEmits(['getData', 'handleSearch']);

const handleApprove = () => {
	const data = {
		Status: STATUS_APPROVE.APPROVED,
		Ma_PR: id_pr,
		Auth: user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		emit('getData');
	});
};

const handleReject = () => {
	const data = {
		Status: STATUS_APPROVE.REJECTED,
		Ma_PR: id_pr,
		Auth: user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		emit('getData');
	});
};

const canApprove = computed(() => {
	const statusFit = statusFit(user?.skylight);
	return status === statusFit;
});

const canEditRequest = computed(() => {
	const phong_ban = id_pr?.split('_')[0];
	return phong_ban === user?.phongban;
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
		<Button v-if="canEditRequest" @click="handleAddDetail">
			<Plus />
			Thêm mới
		</Button>
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
