<script setup>
  import { defineProps, computed } from 'vue'

  const {openDialog, status, value} = defineProps({
    openDialog: {
      type: Boolean,
      required: true
    },
    status: String,
    value: Object
  })

  const emit = defineEmits(['handleClose', 'handleSave'])

  const title = computed(() => {
    switch (status) {
      case "edit":
        return "Sửa yêu cầu"
      case "view":
        return "Chi tiết yêu cầu"
      default:
        return "Thêm yêu cầu"
    }
  })

  const isView = computed(() => { return status === 'view' })

</script>

<template>
  <Dialog :open="openDialog" @update:open="$emit('handleClose')">
    <DialogTrigger as-child>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle class="text-2xl">{{title}}</DialogTitle>
        <DialogDescription></DialogDescription>
      </DialogHeader>
      <div class="flex flex-col gap-y-4">
        <div class="flex gap-4 items-center">
          <span class="min-w-[80px]">Mã vật liệu</span>
          <Select :disabled="isView" :defaultValue="value?.Ma_vat_tu" v-model="value.Ma_vat_tu">
            <SelectTrigger>
              <SelectValue placeholder="Chọn mã vật tư" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="SOFTWARE_01">SOFTWARE_01</SelectItem>
                <SelectItem value="SOFTWARE_02">SOFTWARE_02</SelectItem>
                <SelectItem value="SOFTWARE_03">SOFTWARE_03</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div class="flex gap-4 items-center">
          <span class="min-w-[80px]">Đơn vị</span>
          <Input v-model="value.Don_vi" placeholder="Đơn vị" disabled/>
        </div>
        <div class="flex gap-4 items-center">
          <span class="min-w-[80px]">Mô tả</span>
          <Textarea :disabled="isView" v-model="value.Mo_ta" placeholder="Mô tả" class="resize-none" />
        </div>
        <div class="flex gap-4 items-center">
          <span class="min-w-[80px]">Số lượng</span>
          <Input :disabled="isView" v-model="value.So_luong" type="number" placeholder="Số lượng" />
        </div>
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