<script setup>
import {
	reactive,
	ref,
	toRaw,
	toValue,
	computed,
	onMounted,
	onBeforeUnmount,
} from 'vue';

import { statusApprove, canAddDetail, canOrdered } from '@/utils';
import { STATUS } from '@/constants';
import { Search, Plus } from 'lucide-vue-next';

const { status, id_pr, user } = defineProps({
	status: String,
  id_pr: String,
  user: Object
});
const emit = defineEmits(['handleSearch', 'addDetail', 'approve', 'reject']);

const canAdd = computed(() => canAddDetail(status, id_pr, user));
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
		<Button v-if="canAdd" @click="$emit('addDetail')">
			<Plus />
			Thêm mới
		</Button>
    <div
			v-if="statusApprove(user?.skylight, status)"
			class="flex items-center gap-2"
		>
			<Button variant="destructive" @click="$emit('reject')"
				>Từ chối</Button
			>
			<Button @click="$emit('approve')">Chấp nhận</Button>
		</div>
		<div v-if="canOrdered(user?.skylight, status)">
			<Button @click="$emit('approve')">Xác nhận đặt hàng</Button>
		</div>
	</div>
</template>
