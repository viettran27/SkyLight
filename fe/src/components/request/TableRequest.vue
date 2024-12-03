<script setup>
import { computed } from 'vue';
import {
	canEditRequest,
	formatDate,
	formatISODate,
	statusApprove,
  viewMoney,
	canOrdered
} from '@/utils';
import { Trash, Pencil, X, Check } from 'lucide-vue-next';
import { POSITION } from '@/constants';

const { user, value } = defineProps({
	user: Object,
	value: Array,
});

const emits = defineEmits([
	'deleteRequest',
	'updateRequest',
	'approve',
	'reject',
]);

const canViewMoney = computed(() => {
    return user?.skylight &&
		user?.skylight !== POSITION.REQ &&
		user?.skylight !== POSITION.HOD
})
</script>

<template>
	<Table class="min-w-max relative">
		<TableHeader class="sticky top-0 bg-white z-10">
			<TableRow>
				<TableHead
					class="w-[50px] sticky left-3 bg-white after:content-[''] after:block after:absolute after:-left-3 after:top-0 after:z-20 after:h-[calc(100%+2px)] after:w-3 after:bg-white"
					>STT</TableHead
				>
				<TableHead class="sticky left-[calc(50px+0.75rem)] bg-white"
					>Ma_PR</TableHead
				>
				<TableHead>Thời gian tạo</TableHead>
				<TableHead>Tên PR</TableHead>
				<TableHead>Mục đích</TableHead>
				<TableHead>Ngày cần</TableHead>
        <TableHead v-if="canViewMoney">Tổng tiền</TableHead>
				<TableHead>Trạng thái</TableHead>
				<TableHead>Trưởng bộ phận duyệt</TableHead>
				<TableHead>Kế toán phê duyệt</TableHead>
				<TableHead>Phê duyệt cuối</TableHead>
				<TableHead class="sticky right-3 bg-white"></TableHead>
				<TableHead
					class="w-3 p-0 sticky right-0 z-10 after:content-[''] after:absolute after:bg-white after:block after:w-3 after:h-16 after:top-0"
				></TableHead>
			</TableRow>
		</TableHeader>
		<TableBody>
			<TableRow v-if="value?.length === 0">
				<TableCell colspan="11" class="text-center"
					>Không có yêu cầu nào</TableCell
				>
			</TableRow>
			<TableRow v-for="(row, index) in value" :key="row.Ma_PR">
				<router-link :to="`requests/${row.Ma_PR}`" class="contents">
					<TableCell
						class="sticky left-3 bg-white after:content-[''] after:block after:absolute after:-left-3 after:top-0 after:z-20 after:h-[calc(100%+2px)] after:w-3 after:bg-white"
						>{{ index + 1 }}</TableCell
					>
					<TableCell
						class="sticky left-[calc(50px+0.75rem)] bg-white"
						>{{ row.Ma_PR }}</TableCell
					>
					<TableCell>{{
						formatISODate(row.Thoi_gian_yeu_cau)
					}}</TableCell>
					<TableCell>{{ row.Ten_PR }}</TableCell>
					<TableCell>{{ row.Muc_dich }}</TableCell>
					<TableCell>{{ formatDate(row.Ngay_can) }}</TableCell>
          <TableCell v-if="canViewMoney">{{ viewMoney(row.Tong_so_tien) }}</TableCell>
					<TableCell>{{ row.Trang_thai }}</TableCell>
					<TableCell>{{
						formatISODate(row.Truong_BP_duyet)
					}}</TableCell>
					<TableCell>{{
						formatISODate(row.Ke_toan_phe_duyet)
					}}</TableCell>
					<TableCell>{{
						formatISODate(row.BLD_phe_duyet)
					}}</TableCell>
				</router-link>
				<TableCell
					class="sticky right-3 bg-white flex justify-center items-center"
				>
					<div
						v-if="canEditRequest(row.Trang_thai, row.Ma_PR)"
						class="flex gap-3 items-center"
					>
						<Pencil
							class="cursor-pointer"
							:size="20"
							@click="$emit('updateRequest', row)"
						/>
						<Dialog>
							<DialogTrigger>
								<Trash color="red" :size="20" />
							</DialogTrigger>
							<DialogContent>
								<DialogHeader>
									<DialogTitle class="text-2xl"
										>Xoá yêu cầu</DialogTitle
									>
									<DialogDescription></DialogDescription>
								</DialogHeader>
								<div>
									<p>
										Bạn đang thực hiện xóa yêu cầu có id là
										<b>{{ row.Ma_PR }}</b
										>. Bạn muốn thực hiện thao tác này chứ ?
									</p>
								</div>
								<DialogFooter>
									<DialogClose as-child>
										<Button variant="outline"
											>Quay lại</Button
										>
									</DialogClose>
									<DialogClose as-child>
										<Button
											variant="destructive"
											@click="
												$emit(
													'deleteRequest',
													row.Ma_PR,
												)
											"
											>Xóa</Button
										>
									</DialogClose>
								</DialogFooter>
							</DialogContent>
						</Dialog>
					</div>
					<div
						v-if="statusApprove(user?.skylight, row.Trang_thai)"
						class="flex gap-2"
					>
						<Button
							@click="$emit('reject', row.Ma_PR)"
							variant="destructive"
							size="sm"
							><X :size="20"
						/></Button>
						<Button @click="$emit('approve', row.Ma_PR)" size="sm"
							><Check :size="20"
						/></Button>
					</div>
					<div
						v-if="canOrdered(user?.skylight, row.Trang_thai)"
					>
						<Button @click="$emit('approve', row.Ma_PR)" size="sm"
							><Check :size="20"
						/></Button>
					</div>
				</TableCell>
				<TableCell
					class="w-3 p-0 sticky right-0 z-10 after:content-[''] after:absolute after:bg-white after:block after:w-3 after:h-16 after:top-0"
				></TableCell>
			</TableRow>
		</TableBody>
	</Table>
</template>
