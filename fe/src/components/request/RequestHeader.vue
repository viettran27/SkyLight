<script setup>
import { Search, Plus } from 'lucide-vue-next';
import { POSITION, FILTER } from '@/constants';
import { useFilterStore } from '@/stores/useFilter';

const { user } = defineProps({
	user: Object
})
const emit = defineEmits(['openDialog, handleSearch']);
const filterStore = useFilterStore();

</script>

<template>
	<div class="flex items-center justify-between bg-white px-3 py-5">
		<div class="flex gap-2">
			<div class="relative w-full min-w-[250px] items-center">
				<Input
					id="search"
					type="text"
					@input="$emit('handleSearch', $event.target.value)"
					placeholder="Nhập tên PR"
					class="pl-10"
				/>
				<span
					class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
				>
					<Search class="size-6 text-muted-foreground" />
				</span>
			</div>
			<Select v-model="filterStore.filter" @update:modelValue="filterStore.setFilter($event)">
				<SelectTrigger class="min-w-[200px]">
					<SelectValue placeholder="Chọn loại lọc" />
				</SelectTrigger>
				<SelectContent>
					<SelectGroup>
						<SelectItem :value="FILTER.ALL">Tất cả</SelectItem>
						<SelectItem :value="FILTER.NOT_APPROVE">Chưa duyệt</SelectItem>
						<SelectItem v-if="user?.skylight !== POSITION.REQ" :value="FILTER.APPROVED">Đã duyệt</SelectItem>
						<SelectItem 
							:value="FILTER.ACCT" 
							v-if="user?.skylight !== POSITION.HOD && 
								user?.skylight !== POSITION.ACCT && 
								user?.skylight !== POSITION.CA && 
								user?.skylight !== POSITION.DIR"
						>
							Trưởng bộ phận duyệt
						</SelectItem>
						<SelectItem 
							:value="FILTER.CA" 
							v-if="user?.skylight !== POSITION.ACCT && 
								user?.skylight !== POSITION.CA &&
								user?.skylight !== POSITION.DIR"
						>
							Kế toán duyệt
						</SelectItem>
						<SelectItem 
							:value="FILTER.DIR" 
							v-if="user?.skylight !== POSITION.CA &&
								user?.skylight !== POSITION.DIR"
						>
							Kế toán trưởng duyệt
						</SelectItem>
						<SelectItem 
							:value="FILTER.DIR_ACCEPT" 
							v-if="user?.skylight !== POSITION.DIR"
						>
							Giám đốc duyệt
						</SelectItem>
					</SelectGroup>
				</SelectContent>
			</Select>
		</div>
		<Button v-if="user?.skylight === POSITION.REQ || user?.skylight === POSITION.ACCT" @click="$emit('openDialog')">
			<Plus />
			Thêm mới
		</Button>
	</div>
</template>
