<script setup>
	import { onMounted, onBeforeUnmount } from 'vue';

	import { axiosClient } from '@/lib/axios';
	import { STATUS_APPROVE } from '@/constants';
	
	import { Search, Plus } from 'lucide-vue-next';
	import TableRequest from '@/components/ui-custom/TableRequest.vue';
	import DialogRequest from '@/components/ui-custom/DialogRequest.vue';
  
  const { user, requests } = defineProps({ 
		user: Object,
		requests: Array
	})
	const emits = defineEmits(["getData", "handleSearch"])

	const handleApprove = (ma_pr) => {
		const data = {
			Status: STATUS_APPROVE.APPROVED,
			Ma_PR: ma_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			emits("getData")
		})
	}

	const handleReject = (ma_pr) => {
		const data = {
			Status: STATUS_APPROVE.REJECTED,
			Ma_PR: ma_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			emits("getData")
		})
	}

</script>

<template>
	<div class="flex flex-col h-full">
		<div class="pb-3">
			<h1 class="text-3xl">Yêu cầu</h1>
		</div>
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
							<SelectItem value="not-approved"
								>Chưa duyệt</SelectItem
							>
							<SelectItem value="accountant"
								>Kế toán duyệt</SelectItem
							>
							<SelectItem value="director"
								>Giám đốc duyệt</SelectItem
							>
						</SelectGroup>
					</SelectContent>
				</Select>
			</div>
		</div>
		<div class="bg-white flex-1 pb-3 overflow-auto">
			<TableRequest
				:user="user"
				:value="requests"
				@approve="handleApprove"
				@reject="handleReject"
			/>
		</div>
	</div>
</template>
