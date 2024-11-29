<script setup>
  import { computed } from 'vue'
  const {open, status, value} = defineProps({
    open: Boolean,
    status: String,
    value: Object
  })

  const emit = defineEmits(['closeDialog', 'saveDialog'])
  const title = computed(() => {
    switch (status) {
      case "update":
        return "Sửa yêu cầu"
    
      default:
        return "Thêm yêu cầu"
    }
  })
</script>

<template>
  <Dialog :open="open" @update:open="$emit('closeDialog')">
    <DialogTrigger>
    </DialogTrigger>
    <DialogContent>
      <DialogHeader>
        <DialogTitle class="text-2xl">{{ title }}</DialogTitle>
        <DialogDescription></DialogDescription>
      </DialogHeader>
      <div class="flex flex-col gap-y-4">
        <div class="flex gap-4 items-center">
          <span class="min-w-[130px]">Chọn loại PR</span>
          <Select v-model="value.Ten_PR">
            <SelectTrigger>
              <SelectValue placeholder="Chọn loại PR" />
            </SelectTrigger>
            <SelectContent>
              <SelectGroup>
                <SelectItem value="Máy móc">Máy móc</SelectItem>
                <SelectItem value="Bút">Bút</SelectItem>
              </SelectGroup>
            </SelectContent>
          </Select>
        </div>
        <div class="flex gap-4 items-center">
          <span class="min-w-[130px]">Mục đích</span>
          <Textarea v-model="value.Muc_dich" placeholder="Mục đích" class="resize-none"/>
        </div>
        <div class="flex gap-4 items-center">
          <span class="min-w-[130px]">Ngày mong muốn</span>
          <Input v-model="value.Ngay_can" type="date" class="block"/>
        </div>
      </div>
      <DialogFooter>
        <DialogClose as-child>
          <Button variant="outline">Hủy</Button>
        </DialogClose>
        <Button @click.prevent="$emit('saveDialog')">Lưu</Button>
      </DialogFooter>
    </DialogContent>
  </Dialog>
</template>