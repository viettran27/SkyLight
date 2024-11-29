<script setup>
  import { ref, reactive, toRaw, onMounted, onBeforeUnmount, computed } from 'vue'

  import { useRoute } from "vue-router"
  import { axiosClient } from "@/lib/axios"
  import { debounce } from "lodash"
  import { isApprove, statusFit } from '@/utils'
  import { STATUS_APPROVE } from '@/constants'

  import { Search, Plus, ChevronRight } from 'lucide-vue-next'
  import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

  const { user } = defineProps({ user: Object })

  const tableValue = ref([])
  const search = ref("")
  const dialog = reactive({
		open: false,
		status: 'add',
    value: {}
	})
  
  const route = useRoute()
  const id_pr = route.params.id

  const getData = () => {
    axiosClient.get(`/request_details?ma_pr=${id_pr}`)
    .then(data => {
      tableValue.value = data
    })
  }

  onMounted(() => {
    getData()
  })

  const handleSearch = (value) => {
		if (value) {
			axiosClient.get(`/request_details/search?ma_pr=${id_pr}&ma_vat_tu=${value}`)
			.then(data => {
				tableValue.value = data
			})
		} else {
			getData()
		}
	};

	const handleDebouncedSearch = debounce(() => {
		handleSearch(search.value);
	}, 300); 

	const handleApprove = () => {
		const data = {
			Status: STATUS_APPROVE.APPROVED,
			Ma_PR: id_pr,
			Auth: user?.skylight
		}
		
		axiosClient.post("/requests/approve", data)
		.then(() => {
			getData()
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
			getData()
		})
	}

  const handleViewDetail = (material) => {
    dialog.open = true
    dialog.status = "view"
    dialog.value = structuredClone(toRaw(material))
  }

  const canApprove = computed(() => {
    const status = statusFit(user?.skylight)
    return tableValue.value?.[0]?.["Trang_thai"] === status
  })

  onBeforeUnmount(() => {
		handleDebouncedSearch.cancel();
	});
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
          v-model="search"
          @input="handleDebouncedSearch"
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
        :value="tableValue"
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