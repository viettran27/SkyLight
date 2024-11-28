<script setup>
  import { Trash, Pencil } from "lucide-vue-next"
  import { defineProps } from 'vue'
  const { value } = defineProps({
    value: Array
  })

  const emits = defineEmits(['deleteRequest', 'updateRequest'])
</script>

<template>
  <Table>
    <TableHeader>
      <TableRow>
        <TableHead class="w-[100px]">STT</TableHead>
        <TableHead>ID</TableHead>
        <TableHead>Thời gian tạo</TableHead>
        <TableHead>Trưởng bộ phận duyệt</TableHead>
        <TableHead>Kế toán phê duyệt</TableHead>
        <TableHead>Phê duyệt cuối</TableHead>
        <TableHead>Trạng thái</TableHead>
        <TableHead></TableHead>
      </TableRow>
    </TableHeader>
    <TableBody>
      <TableRow v-for="(row, index) in value" :key="row.ID">
        <router-link :to="`requests/${row.ID}`" class="contents">
          <TableCell>{{ index + 1 }}</TableCell>
          <TableCell>{{ row.ID }}</TableCell>
          <TableCell>{{ row.Thoi_gian_yeu_cau }}</TableCell>
          <TableCell>{{ row.Truong_BP_duyet }}</TableCell>
          <TableCell>{{ row.Ke_toan_phe_duyet }}</TableCell>
          <TableCell>{{ row.BLD_phe_duyet }}</TableCell>
          <TableCell>{{ row.Trang_thai }}</TableCell>
        </router-link>
        <TableCell>
            <div v-if="row.Trang_thai === 'Đang đợi duyệt'">
              <div class="flex gap-3 items-center">
                <Pencil class="cursor-pointer" :size="20" @click="$emit('updateRequest', row.ID)"/>
                <Dialog>
                  <DialogTrigger>
                    <Trash color="red" :size="20"/>
                  </DialogTrigger>
                  <DialogContent>
                    <DialogHeader>
                      <DialogTitle class="text-2xl">Xoá yêu cầu</DialogTitle>
                      <DialogDescription></DialogDescription>
                    </DialogHeader>
                    <div>
                      <p>Bạn đang thực hiện xóa yêu cầu có id là <b>{{ row.ID}}</b>. Bạn muốn thực hiện thao tác này chứ ?</p>
                    </div>
                    <DialogFooter>
                      <DialogClose>
                        <Button variant="outline">Quay lại</Button>
                      </DialogClose>
                      <Button variant="destructive" @click="$emit('deleteRequest' ,row.ID)">Xóa</Button>
                    </DialogFooter>
                  </DialogContent>
                </Dialog>
              </div>
            </div>
        </TableCell>
      </TableRow>
    </TableBody>
  </Table>
</template>