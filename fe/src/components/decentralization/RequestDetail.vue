<script setup>
  import { reactive, ref, toRaw, toValue, onMounted, onBeforeUnmount } from 'vue'

  import { axiosClient } from '@/lib/axios'
  import { isApprove } from '@/utils'

  import { Search, Plus, ChevronRight } from 'lucide-vue-next'
  import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

  const INIT_DIALOG = {
    Ma_vat_tu: "",
    Don_vi: "",
    Mo_ta: "",
    So_luong: 1
  }

  const dialog = reactive({
    open: false,
    status: "add",
    value: INIT_DIALOG
  })

  const { details, id_pr } = defineProps({ 
    details: Array,
    id_pr: String
  })
  const emits = defineEmits(["getData", "handleSearch"])

  const handleAddDetail = () => {
    dialog.open = true
    dialog.status = "add"
    dialog.value = structuredClone(INIT_DIALOG)
  }

  const handleEdit = (material) => {
    dialog.open = true
    dialog.status = "update"
    dialog.value = structuredClone(toRaw(material))
  }
  
  const handleViewDetail = (material) => {
    dialog.open = true
    dialog.status = "view"
    dialog.value = structuredClone(toRaw(material))
  }

  const handleDeleteDetail = (id) => {
    axiosClient.delete(`/request_details/${id}`)
    .then(() => {
      emits("getData")
    })
  }

  const handleSaveDialog = async () => {
    const value = toValue(dialog.value)
    switch (dialog.status) {
      case "update":
        await axiosClient.put(`/request_details/${value.ID}`, value)
        break;
        
      default:
        const data = {
          Ma_PR: id_pr,
          ...value
        }
        await axiosClient.post("/request_details", data)
        break;
    }

    emits("getData")
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
    <div class="flex justify-between item-center bg-white px-3 py-5">
      <div class="relative w-full max-w-[250px] items-center">
        <Input
          id="search"
          type="text"
          @input="$emits('handleSearch', $event.target.value)"
          placeholder="Nhập mã vật liệu"
          class="pl-10"
        />
        <span
          class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
        >
          <Search class="size-6 text-muted-foreground" />
        </span>
      </div>
      <Button @click='handleAddDetail'>
        <Plus /> 
        Thêm mới
      </Button>
    </div>
    <div class="bg-white flex-1 pb-3 overflow-auto">
      <TableDetail
        :value="details"
        @edit-detail="handleEdit"
        @view-detail="handleViewDetail"
        @delete-detail="handleDeleteDetail"
      />
    </div>
    <DialogDetail 
      :value="dialog.value"
      :status="dialog.status"
      :open-dialog="dialog.open"
      @handle-save="handleSaveDialog"
      @handle-close="() => dialog.open = false"
    />
  </div>
</template>