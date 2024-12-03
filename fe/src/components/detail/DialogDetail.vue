<script setup>
import { computed } from 'vue';

const { openDialog, status, value, isAcct } = defineProps({
	openDialog: {
		type: Boolean,
		required: true,
	},
	status: String,
	value: Object,
	isAcct: {
		type: Boolean,
		default: false,
	},
});

const emit = defineEmits(['handleClose', 'handleSave']);

const title = computed(() => {
	switch (status) {
		case 'update':
			return 'Sửa vật liệu';
		case 'view':
			return 'Chi tiết vật liệu';
		default:
			return 'Thêm vật liệu';
	}
});

const isView = computed(() => {
	return status === 'view';
});
</script>

<template>
	<Dialog :open="openDialog" @update:open="$emit('handleClose')">
		<DialogTrigger as-child> </DialogTrigger>
		<DialogContent>
			<DialogHeader>
				<DialogTitle class="text-2xl">{{ title }}</DialogTitle>
				<DialogDescription></DialogDescription>
			</DialogHeader>
			<div class="flex flex-col gap-y-4">
				<div class="flex gap-4 items-center">
					<span class="min-w-[100px]">Mã vật tư</span>
					<Select
						:disabled="isView"
						:defaultValue="value?.Ma_vat_tu"
						v-model="value.Ma_vat_tu"
						@update:modelValue="value.Don_vi = 'License'"
					>
						<SelectTrigger>
							<SelectValue placeholder="Chọn mã vật tư" />
						</SelectTrigger>
						<SelectContent>
							<SelectGroup>
								<SelectItem value="SOFTWARE_01"
									>SOFTWARE_01</SelectItem
								>
								<SelectItem value="SOFTWARE_02"
									>SOFTWARE_02</SelectItem
								>
								<SelectItem value="SOFTWARE_03"
									>SOFTWARE_03</SelectItem
								>
							</SelectGroup>
						</SelectContent>
					</Select>
				</div>
				<div class="flex gap-4 items-center">
					<span class="min-w-[100px]">Đơn vị</span>
					<Input
						v-model="value.Don_vi"
						placeholder="Đơn vị"
						disabled
					/>
				</div>
				<div class="flex gap-4 items-center">
					<span class="min-w-[100px]">Mô tả</span>
					<Textarea
						:disabled="isView"
						v-model="value.Mo_ta"
						placeholder="Mô tả"
						class="resize-none"
					/>
				</div>
				<div class="flex gap-4 items-center">
					<span class="min-w-[100px]">Số lượng</span>
					<Input
						:disabled="isView"
						v-model="value.So_luong"
						type="number"
						placeholder="Số lượng"
					/>
				</div>
				<template v-if="isAcct">
					<div class="flex gap-4 items-center">
						<span class="min-w-[100px]">Đơn giá</span>
						<MoneyInput v-model:value="value.Don_gia" />
					</div>
					<div class="flex gap-4 items-center">
						<span class="min-w-[100px]">Nhà cung cấp</span>
						<Input
							:disabled="isView"
							v-model="value.Nha_cung_cap"
							placeholder="Nhà cung cấp"
						/>
					</div>
					<div class="flex gap-4 items-center">
						<span class="min-w-[100px]">Ngày dữ kiến</span>
						<Input
							:disabled="isView"
							v-model="value.Ngay_ve_du_kien"
							type="date"
							class="block"
							placeholder="Số lượng"
						/>
					</div>
				</template>
			</div>
			<DialogFooter>
				<DialogClose as-child>
					<Button variant="outline">Quay lại</Button>
				</DialogClose>
				<Button v-if="!isView" @click="$emit('handleSave')">Lưu</Button>
			</DialogFooter>
		</DialogContent>
	</Dialog>
</template>
