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

import { isApprove } from '@/utils';
import { STATUS } from '@/constants';
import { Search, Plus } from 'lucide-vue-next';

const { status } = defineProps({
	status: String,
});
const emit = defineEmits(['handleSearch', 'addDetail']);

const canAdd = computed(() => {
	return (
		!status ||
		status === STATUS.HOD
	);
});

const canApprove = computed(() => {
  status === STATUS.ACCT_EDIT
})
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
	</div>
</template>
