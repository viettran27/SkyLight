<script setup>
	import { Search, Plus, Trash } from 'lucide-vue-next';

	const requests = [
		{
			ID: 'IED_01',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
		{
			ID: 'IED_01',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
		{
			ID: 'IED_01',
			Thoi_gian_yeu_cau: '20/11/2024 15:20',
			Truong_BP_duyet: '20/11/2024 15:20',
			Ke_toan_phe_duyet: '20/11/2024 15:20',
			BLD_phe_duyet: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt"
		},
	]
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
				<Button>
					<Plus class="mr-1" />
					Thêm mới
				</Button>
			</div>
			<div class="mt-5">
				<Table>
					<TableHeader>
						<TableRow>
							<TableHead class="w-[100px]">STT</TableHead>
							<TableHead>ID</TableHead>
							<TableHead>Thời gian tạo</TableHead>
							<TableHead>Thời gian trưởng bp duyệt</TableHead>
							<TableHead>Thời gian kế toán phê duyệt</TableHead>
							<TableHead>Thời gian blđ phê duyệt</TableHead>
							<TableHead>Trạng thái</TableHead>
							<TableHead></TableHead>
						</TableRow>
					</TableHeader>
					<TableBody>
						<TableRow v-for="(request, index) in requests" :key="request.ID">
							<router-link :to="`requests/${request.ID}`" class="contents">
								<TableCell>{{ index + 1 }}</TableCell>
								<TableCell>{{ request.ID }}</TableCell>
								<TableCell>{{ request.Thoi_gian_yeu_cau }}</TableCell>
								<TableCell>{{ request.Truong_BP_duyet }}</TableCell>
								<TableCell>{{ request.Ke_toan_phe_duyet }}</TableCell>
								<TableCell>{{ request.BLD_phe_duyet }}</TableCell>
								<TableCell>{{ request.Trang_thai }}</TableCell>
							</router-link>
							<TableCell>
									<div v-if="request.Trang_thai === 'Đang đợi duyệt'">
										<Trash color="red" :size="20"/>
									</div>
							</TableCell>
						</TableRow>
					</TableBody>
				</Table>
			</div>
		</div>
	</div>
</template>
