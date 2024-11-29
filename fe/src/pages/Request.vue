<script setup>
	import { ref, watch, onMounted, onBeforeUnmount } from 'vue'
	
	import { useAuthStore } from '@/stores/useAuth';
	
	import { axiosClient } from '@/lib/axios';
	import { debounce } from 'lodash';
	import { isApprove } from '@/utils';

	import Request from '@/components/decentralization/Request.vue';
	import Approve from '@/components/decentralization/Approve.vue'

	const requests = ref([])
	const authStore = useAuthStore()

	const getData = () => {
		axiosClient.get(`/requests?phong_ban=${authStore?.user?.phongban}&chuc_vu=${authStore?.user?.skylight}`)
		.then(data => {
			requests.value = data
		})
	}

	watch([authStore], () => {
		if (authStore.user) getData()
	})
	
	onMounted(() => {
		getData()
	})

	const handleSearch = (value) => {
		if (value) {
			axiosClient.get(`/requests/search?ma_pr=${value}`)
			.then(data => {
				requests.value = data
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
	<Request 
		:user="authStore?.user" 
		:requests="requests"
		@get-data="getData" 
		@handle-search="handleDebouncedSearch" 
		v-if="authStore?.user?.skylight === 'req'"
	/>
	<Approve 
		:user="authStore?.user" 
		:requests="requests"
		@get-data="getData" 
		@handle-search="handleDebouncedSearch" 
		v-if="isApprove(authStore?.user?.skylight)"
	/>
</template>
