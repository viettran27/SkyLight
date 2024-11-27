<script setup>
  import { reactive, ref, toRaw, toValue } from 'vue'
  import { useRoute } from "vue-router"
  import { Search, Plus, ChevronRight } from 'lucide-vue-next'
  import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

  const INIT_DIALOG = {
    Ma_vat_lieu: "",
    Don_vi: "",
    Mo_ta: "",
    So_luong: 0
  }

  const dialog = reactive({
    open: false,
    status: "add",
    rowIndex: -1
  })

  const dialogValue = ref(INIT_DIALOG)

  const tableValue = ref([
		{
			Ma_vat_tu: 'SOFTWARE_01',
			Ten_vat_tu: 'Power BI',
			Don_vi: 'License',
			So_luong: 1,
      Mo_ta: "Phần mềm biểu đồ",
			Ngay_ve_du_kien: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt",
      Thanh_tien: 1000000
		},
		{
			Ma_vat_tu: 'SOFTWARE_02',
			Ten_vat_tu: 'Power BI',
			Don_vi: 'License',
			So_luong: 1,
      Mo_ta: "Phần mềm biểu đồ",
			Ngay_ve_du_kien: '20/11/2024 15:20',
			Trang_thai: "Đang đợi duyệt",
      Thanh_tien: 1000000
		},
		{
			Ma_vat_tu: 'SOFTWARE_03',
			Ten_vat_tu: 'Power BI',
			Don_vi: 'License',
			So_luong: 1,
      Mo_ta: "Phần mềm biểu đồ",
			Ngay_ve_du_kien: '20/11/2024 15:20',
			Trang_thai: "Trưởng bộ phận đã duyệt",
      Thanh_tien: 1000000
		},
	])

  const route = useRoute()
  const id_pr = route.params.id

  const handleAddDetail = () => {
    dialog.open = true
    dialog.status = "add"
    dialog.rowIndex = -1
    dialogValue.value = INIT_DIALOG
  }

  const handleEdit = (index, material) => {
    dialog.open = true
    dialog.status = "edit"
    dialog.rowIndex = index
    dialogValue.value = structuredClone(toRaw(material))
  }
  
  const handleViewDetail = (index, material) => {
    dialog.open = true
    dialog.status = "view"
    dialog.rowIndex = index
    dialogValue.value = structuredClone(toRaw(material))
  }

  const handleDeleteDetail = (index, material) => {
    tableValue.value.splice(index, 1)
  }

  const handleSaveDialog = () => {
    const value = toValue(dialogValue)
    switch (dialog.status) {
      case "edit":
        tableValue.value[dialog.rowIndex] = value
        break;
    
      default:
        break;
    }
    dialog.open = false
  }
</script>

<template>
  <div class="flex flex-col h-full">
    <div class="flex items-end gap-2 pb-3">
      <router-link to="/requests">
        <h1>Yêu cầu</h1>
      </router-link>
      <ChevronRight />
      <h1>{{ id_pr }}</h1>
    </div>
    <div class="bg-white flex-1 p-3">
      <div class="flex justify-between item-center">
        <div class="relative w-full max-w-[250px] items-center">
          <Input
            id="search"
            type="text"
            placeholder="Nhập tên vật liệu"
            class="pl-10"
          />
          <span
            class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
          >
            <Search class="size-6 text-muted-foreground" />
          </span>
        </div>
        <Button @click='handleAddDetail'>
          <Plus /> Thêm mới
        </Button>
      </div>
      <div class="mt-5">
        <TableDetail
          :value="tableValue"
          @edit-detail="handleEdit"
          @view-detail="handleViewDetail"
          @delete-detail="handleDeleteDetail"
        />
      </div>
    </div>
    <DialogDetail 
      :value="dialogValue"
      :status="dialog.status"
      :open-dialog="dialog.open"
      @handle-save="handleSaveDialog"
      @handle-close="() => dialog.open = false"
    />
  </div>
</template>