<script setup>
  import { ref, onMounted, onBeforeUnmount } from 'vue'
  import { useAuthStore } from '@/stores/useAuth';
  
  import { useRoute } from "vue-router"
  import { axiosClient } from '@/lib/axios';
	import { debounce } from 'lodash';
  import { isApprove } from '@/utils'
  
  import ApproveDetail from '@/components/decentralization/ApproveDetail.vue'
  import RequestDetail from '@/components/decentralization/RequestDetail.vue'

  const details = ref([])
  const authStore = useAuthStore() 

  const route = useRoute()
  const id_pr = route.params.id

  const getData = () => {
    axiosClient.get(`/request_details?ma_pr=${id_pr}`)
    .then(data => {
      details.value = data
    })
  }

  onMounted(() => {
    console.log("mount")
    getData()
  })

  const handleSearch = (value) => {
		if (value) {
			axiosClient.get(`/request_details/search?ma_pr=${id_pr}&ma_vat_tu=${value}`)
			.then(data => {
				details.value = data
			})
		} else {
			getData()
		}
	};

	const handleDebouncedSearch = debounce((value) => {
		handleSearch(value);
	}, 300); 

  onBeforeUnmount(() => {
		handleDebouncedSearch.cancel();
	});
</script>

<template>
  <RequestDetail
    :id_pr="id_pr"
    :details="details"
		@get-data="getData" 
		@handle-search="handleDebouncedSearch" 
    v-if="authStore?.user?.skylight === 'req'"
  />
  <ApproveDetail
    :id_pr="id_pr"
    :details="details"
    @get-data="getData" 
    @handle-search="handleDebouncedSearch" 
    :user="authStore?.user" v-if="isApprove(authStore?.user?.skylight)"
  />
</template>