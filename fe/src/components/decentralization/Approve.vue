<script setup>
import { Search } from 'lucide-vue-next';

const emits = defineEmits(['handleSearch']);
</script>

<template>
	<div class="flex items-center justify-between bg-white px-3 py-5">
		<div class="flex gap-2">
			<div class="relative w-full min-w-[250px] items-center">
				<Input
					id="search"
					type="text"
					@input="$emits('handleSearch', $event.target.value)"
					placeholder="Nhập tên mã PR"
					class="pl-10"
				/>
				<span
					class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
				>
					<Search class="size-6 text-muted-foreground" />
				</span>
			</div>
			<Select default-value="all">
				<SelectTrigger class="min-w-[150px]">
					<SelectValue placeholder="Chọn loại lọc" />
				</SelectTrigger>
				<SelectContent>
					<SelectGroup>
						<SelectItem value="all">Tất cả</SelectItem>
						<SelectItem value="not-approved">Chưa duyệt</SelectItem>
						<SelectItem value="accountant"
							>Kế toán duyệt</SelectItem
						>
						<SelectItem value="director">Giám đốc duyệt</SelectItem>
					</SelectGroup>
				</SelectContent>
			</Select>
		</div>
	</div>
</template>
