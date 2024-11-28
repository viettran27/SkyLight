<script setup>
	import { ref, reactive } from 'vue';
	import { useRouter } from 'vue-router'
	import { Search, Plus } from 'lucide-vue-next';
	import TableRequest from '@/components/ui-custom/TableRequest.vue';
	import DialogRequest from '@/components/ui-custom/DialogRequest.vue';

	const fake_request = [
		{
			ID: 'IED_01',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
		{
			ID: 'IED_02',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
		{
			ID: 'IED_03',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
	]

	const INIT_REQUEST = {
		Ten_PR: "",
		Muc_dich: "",
		Ngay_can: ""
	}

	const dialog = reactive({
		open: false,
		status: 'add'
	})
	const requests = ref(fake_request)
	const dialogValue = ref(INIT_REQUEST)

	const router = useRouter()

	const handleOpenDialog = () => {
		dialog.open = true
		dialog.status = "add"
	}

	const handleCloseDialog = () => {
		dialog.open = false
		dialogValue.value = INIT_REQUEST
	}

	const handleSaveDialog = () => {
		switch (dialog.status) {
			case "update":
				dialog.open = false
				break;
		
			default:
				router.push("/requests/IED_01")
				break;
		}
	}

	const handleUpdateRequest = (id) => {
		dialog.open = true
		dialog.status = "update"
		dialogValue.value = requests.value.find(request => request.ID === id)
	}

	const handleDeleteRequest = (id) => {
		requests.value = requests.value.filter(request => request.ID !== id)
	}
</script>

<template>
	<div class="flex flex-col h-full">
		<div class="pb-3">
			<h1 class="text-3xl">Yêu cầu</h1>
		</div>
		<div class="bg-white flex-1 p-3">
			<div class="flex items-center justify-between">
				<div class="flex gap-2">
					<div class="relative w-full min-w-[250px] items-center">
						<Input
							id="search"
							type="text"
							placeholder="Nhập tên ID"
							class="pl-10"
						/>
						<span
							class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
						>
							<Search class="size-6 text-muted-foreground" />
						</span>
					</div>
					<Select>
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
					<Plus class="mr-1" />
					Thêm mới
				</Button>
			</div>
			<div class="mt-5">
				<TableRequest 
					:value="requests"
					@update-request="handleUpdateRequest"
					@delete-request="handleDeleteRequest"
				/>
			</div>
		</div>
		<DialogRequest 
			:open="dialog.open"
			:status="dialog.status"
			:value="dialogValue"
			@close-dialog="handleCloseDialog"
			@save-dialog="handleSaveDialog"
		/>
	</div>
</template>
