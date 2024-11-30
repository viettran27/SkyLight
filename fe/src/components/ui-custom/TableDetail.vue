<script setup>
import { Trash, Pencil } from 'lucide-vue-next';
import { computed } from 'vue';
import { useAuthStore } from '@/stores/useAuth';
import { canEditDetail, viewMoney } from '@/utils';
import { POSITION } from '@/constants';

const { value, id_pr } = defineProps({
	value: {
		type: Array,
		required: true,
	},
	id_pr: String,
});
const emit = defineEmits(['editDetail', 'viewDetail', 'getData']);

const authStore = useAuthStore();

const handleDeleteDetail = (id) => {
	axiosClient.delete(`/request_details/${id}`).then(() => {
		emit('getData');
	});
};

const canViewMoney = computed(() => {
	return (
		authStore.user?.skylight &&
		authStore.user?.skylight !== POSITION.REQ &&
		authStore.user?.skylight !== POSITION.HOD
	);
});
</script>

<template>
	<Table class="min-w-max relative">
		<TableHeader class="sticky top-0 bg-white z-10">
			<TableRow>
				<TableHead
					class="w-[50px] sticky left-3 bg-white after:content-[''] after:block after:absolute after:-left-3 after:top-0 after:z-20 after:h-[calc(100%+1px)] after:w-3 after:bg-white"
					>STT</TableHead
				>
				<TableHead class="sticky left-[calc(50px+0.75rem)] bg-white"
					>Mã vật tư</TableHead
				>
				<TableHead>Mô tả</TableHead>
				<TableHead>Đơn vị</TableHead>
				<TableHead>Số lượng</TableHead>
				<TableHead>Ngày về dự kiến</TableHead>
				<TableHead v-if="canViewMoney">Thành tiền</TableHead>
				<TableHead>Trạng thái</TableHead>
				<TableHead
					class="sticky right-3 bg-white flex justify-center"
				></TableHead>
				<TableHead
					class="w-3 p-0 sticky right-0 z-10 after:content-[''] after:absolute after:bg-white after:block after:w-3 after:h-16 after:top-0"
				></TableHead>
			</TableRow>
		</TableHeader>
		<TableBody>
			<TableRow v-if="value.length === 0">
				<TableCell colspan="9" class="text-center"
					>Không có vật tư nào</TableCell
				>
			</TableRow>
			<TableRow
				v-for="(row, index) in value"
				:key="row.ID"
				class="cursor-pointer"
				@click="$emit('viewDetail', row)"
			>
				<TableCell
					class="sticky left-3 bg-white after:content-[''] after:block after:absolute after:-left-3 after:top-0 after:z-20 after:h-[calc(100%+1px)] after:w-3 after:bg-white"
					>{{ index + 1 }}</TableCell
				>
				<TableCell class="sticky left-[calc(50px+0.75rem)] bg-white">{{
					row.Ma_vat_tu
				}}</TableCell>
				<TableCell>{{ row.Mo_ta }}</TableCell>
				<TableCell>{{ row.Don_vi }}</TableCell>
				<TableCell>{{ row.So_luong }}</TableCell>
				<TableCell>{{ row.Ngay_ve_du_kien }}</TableCell>
				<TableCell v-if="canViewMoney">{{
					viewMoney(row.Thanh_tien)
				}}</TableCell>
				<TableCell>{{ row.Trang_thai }}</TableCell>
				<TableCell
					class="sticky right-3 bg-white flex justify-center h-16"
				>
					<div
						class="flex gap-3 items-center"
						v-if="canEditDetail(row.Trang_thai, id_pr)"
					>
						<Pencil
							class="cursor-pointer"
							:size="20"
							@click.stop="$emit('editDetail', row)"
						/>
						<Dialog v-if="authStore.user?.skylight === 'req'">
							<DialogTrigger as-child>
								<Trash @click.stop color="red" :size="20" />
							</DialogTrigger>
							<DialogContent>
								<DialogHeader>
									<DialogTitle class="text-2xl"
										>Xác nhận xóa</DialogTitle
									>
									<DialogDescription></DialogDescription>
								</DialogHeader>
								<div>
									<p>
										Bạn đang thực hiện xóa vật liệu có id là
										<b>{{ row.Ma_vat_tu }}</b
										>. Bạn muốn thực hiện thao tác này chứ ?
									</p>
								</div>
								<DialogFooter>
									<DialogClose as-child>
										<Button variant="outline">Hủy</Button>
									</DialogClose>
									<DialogClose as-child>
										<Button
											variant="destructive"
											@click="
												() => handleDeleteDetail(row.ID)
											"
											>Xóa</Button
										>
									</DialogClose>
								</DialogFooter>
							</DialogContent>
						</Dialog>
					</div>
				</TableCell>
				<TableCell
					class="w-3 p-0 sticky right-0 z-10 after:content-[''] after:absolute after:bg-white after:block after:w-3 after:h-16 after:top-0"
				></TableCell>
			</TableRow>
		</TableBody>
	</Table>
</template>
