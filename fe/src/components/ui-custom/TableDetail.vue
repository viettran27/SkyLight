<script setup>
  import { Edit, Trash, Pencil } from "lucide-vue-next"
  import { defineProps, computed } from "vue"
  import { useAuthStore } from "@/stores/useAuth";
  
  const { value } = defineProps({
    value: {
      type: Array,
      required: true
    }
  })

  const authStore = useAuthStore();

  const emit = defineEmits(['editDetail', 'viewDetail', 'deleteDetail'])

  const viewMoney = (money) => {
    return money.toLocaleString('vi-VN', { style: 'currency', currency: 'VND' })
  }

  const canViewMoney = computed(() => {
    return authStore.user?.skylight !== 'req' && authStore.user?.skylight !== 'hod'
  })
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead class="w-[100px]">STT</TableHead>
        <TableHead>Mã vật tư</TableHead>
        <TableHead>Tên vật tư</TableHead>
        <TableHead>Đơn vị</TableHead>
        <TableHead>Số lượng</TableHead>
        <TableHead>Ngày về dự kiến</TableHead>
        <TableHead>Trạng thái</TableHead>
        <TableHead v-if="canViewMoney">Thành tiền</TableHead>
        <TableHead></TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="(row, index) in value" :key="row.Ma_vat_tu" class="cursor-pointer" @click="$emit('viewDetail', index, row)">
        <TableCell>{{ index + 1 }}</TableCell>
        <TableCell>{{ row.Ma_vat_tu }}</TableCell>
        <TableCell>{{ row.Ten_vat_tu }}</TableCell>
        <TableCell>{{ row.Don_vi }}</TableCell>
        <TableCell>{{ row.So_luong }}</TableCell>
        <TableCell>{{ row.Ngay_ve_du_kien }}</TableCell>
        <TableCell>{{ row.Trang_thai }}</TableCell>
        <TableCell v-if="canViewMoney">{{ viewMoney(row.Thanh_tien) }}</TableCell>
        <TableCell>
          <div class="flex gap-3 items-center" v-if="row.Trang_thai === 'Đang đợi duyệt'">
            <Pencil class="cursor-pointer" :size="20" @click.stop="$emit('editDetail', index, row)"/>
            <Dialog>
              <DialogTrigger as-child>
                <Trash @click.stop color="red" :size="20"/>
              </DialogTrigger>
              <DialogContent>
                <DialogHeader>
                  <DialogTitle class="text-2xl">Xác nhận xóa</DialogTitle>
                  <DialogDescription></DialogDescription>
                </DialogHeader>
                <div>
                  <p>Bạn đang thực hiện xóa vật liệu có id là <b>{{ row.Ma_vat_tu }}</b>. Bạn muốn thực hiện thao tác này chứ ?</p>
                </div>
                <DialogFooter>
                  <DialogClose as-child>
                    <Button variant="outline">Hủy</Button>
                  </DialogClose>
                  <DialogClose as-child>
                    <Button variant="destructive" @click="$emit('deleteDetail', index, row)">Xóa</Button>
                  </DialogClose>
                </DialogFooter>
              </DialogContent>
            </Dialog>
          </div>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>