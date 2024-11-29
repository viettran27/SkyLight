<script setup>
	import { ref, reactive, onMounted, onBeforeUnmount } from 'vue';
	
	import { useRouter } from 'vue-router'

	import { axiosClient } from '@/lib/axios';
	import { debounce } from 'lodash';
	import { STATUS_APPROVE } from '@/constants';
	
	import { Search, Plus } from 'lucide-vue-next';
	import TableRequest from '@/components/ui-custom/TableRequest.vue';
	import DialogRequest from '@/components/ui-custom/DialogRequest.vue';

	const requests = ref([])
	const search = ref("")
  
	const router = useRouter()
  const { user } = defineProps({ user: Object })

	const getData = () => {
		axiosClient.get(`/requests?phong_ban=${user.phongban}&chuc_vu=${user.skylight}`)
		.then(data => {
			requests.value = data
		})
	}

	onMounted(() => {
		getData()
	})

	const handleSearch = (value) => {
		if (value) {
			axiosClient.get(`/requests/search?ma_pr=${value}`)
			.then(data => {
				requests.value = data
			})
		} else {
			getData()
		}
	};

	const handleDebouncedSearch = debounce(() => {
		handleSearch(search.value);
	}, 300); 

	const handleApprove = (ma_pr) => {
		const data = {
			Status: STATUS_APPROVE.APPROVED,
			Ma_PR: ma_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			getData()
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
			getData()
		})
	}

	onBeforeUnmount(() => {
		handleDebouncedSearch.cancel();
	});
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
						v-model="search"
						@input="handleDebouncedSearch"
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
