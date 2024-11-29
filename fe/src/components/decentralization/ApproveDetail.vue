<script setup>
  import { ref, reactive, toRaw, onMounted, onBeforeUnmount, computed } from 'vue'

  import { axiosClient } from "@/lib/axios"
  import { isApprove, statusFit } from '@/utils'
  import { STATUS_APPROVE } from '@/constants'

  import { Search, Plus, ChevronRight } from 'lucide-vue-next'
  import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

  const { user, details, id_pr } = defineProps({ 
    user: Object,
    details: Array,
    id_pr: String
  })
  const emits = defineEmits(["getData", "handleSearch"])
  
  const dialog = reactive({
		open: false,
		status: 'add',
    value: {}
	})

	const handleApprove = () => {
		const data = {
			Status: STATUS_APPROVE.APPROVED,
			Ma_PR: id_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			emits("getData")
		})
	}

	const handleReject = () => {
		const data = {
			Status: STATUS_APPROVE.REJECTED,
			Ma_PR: id_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			emits("getData")
		})
	}

  const handleViewDetail = (material) => {
    dialog.open = true
    dialog.status = "view"
    dialog.value = structuredClone(toRaw(material))
  }

  const canApprove = computed(() => {
    const status = statusFit(user?.skylight)
    return details?.[0]?.["Trang_thai"] === status
  })
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
          @input="$emit('handleSearch', $event.target.value)"
          placeholder="Nhập mã vật liệu"
          class="pl-10"
        />
        <span
          class="absolute start-0 inset-y-0 flex items-center justify-center px-2"
        >
          <Search class="size-6 text-muted-foreground" />
        </span>
      </div>
      <div v-if="isApprove(user?.skylight) && canApprove" class="flex items-center gap-2">
        <Button variant="destructive" @click="handleReject">Không duyệt</Button>
        <Button @click="handleApprove">Duyệt</Button>
      </div>
    </div>
    <div class="bg-white flex-1 pb-3 overflow-auto">
      <TableDetail
        :value="details"
        @view-detail="handleViewDetail"
      />
    </div>
    <DialogDetail 
      :value="dialog.value"
      :status="dialog.status"
      :open-dialog="dialog.open"
      @handle-close="() => dialog.open = false"
    />
  </div>
</template>