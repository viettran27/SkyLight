<script setup>
	import { ref, reactive, onMounted, onBeforeUnmount } from 'vue';
	import { useRouter } from 'vue-router'
	import { Search, Plus } from 'lucide-vue-next';
	import { axiosClient } from '@/lib/axios';
	import { useAuthStore } from '@/stores/useAuth';
	import { debounce } from 'lodash';
	import TableRequest from '@/components/ui-custom/TableRequest.vue';
	import DialogRequest from '@/components/ui-custom/DialogRequest.vue';

	const INIT_REQUEST = {
		Ten_PR: "",
		Muc_dich: "",
		Ngay_can: ""
	}

	const { user } = defineProps({ user: Object })

	const dialog = reactive({
		open: false,
		status: 'add',
		value: INIT_REQUEST
	})
	const requests = ref([])
	const search = ref("")

	const router = useRouter()

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

	const handleOpenDialog = () => {
		dialog.open = true
		dialog.status = "add"
		dialog.value = INIT_REQUEST
	}

	const handleCloseDialog = () => {
		dialog.open = false
		dialog.value = INIT_REQUEST
	}

	const handleSaveDialog = () => {
		const data = {
			Ten_PR: dialog.value.Ten_PR,
			Muc_dich: dialog.value.Muc_dich,
			Ngay_can: dialog.value.Ngay_can,
			Phong_ban: user.phongban,
			Nguoi_yeu_cau: user.hoten
		}

		switch (dialog.status) {
			case "update":
				axiosClient.put(`/requests/${dialog.value.Ma_PR}`, data)
				.then(() => {
					dialog.open = false
					getData()
				})
				break;
		
			default:
				axiosClient.post("/requests", data)
				.then((request) => {
					router.push(`/requests/${request.Ma_PR}`)
				})
				break;
		}
	}

	const handleUpdateRequest = (request) => {
		dialog.open = true
		dialog.status = "update"
		dialog.value = request
	}

	const handleDeleteRequest = (ma_pr) => {
		axiosClient.delete(`/requests/${ma_pr}`)
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
			<Button @click="handleOpenDialog">
				<Plus />
				Thêm mới
			</Button>
		</div>
		<div class="bg-white flex-1 pb-3 overflow-auto">
			<TableRequest 
				:value="requests"
				@update-request="handleUpdateRequest"
				@delete-request="handleDeleteRequest"
			/>
		</div>
		<DialogRequest 
			:open="dialog.open"
			:status="dialog.status"
			:value="dialog.value"
			@close-dialog="handleCloseDialog"
			@save-dialog="handleSaveDialog"
		/>
	</div>
</template>
