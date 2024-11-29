<script setup>
	import Request from '@/components/decentralization/Request.vue';
	import Approve from '@/components/decentralization/Approve.vue'
	import { useAuthStore } from '@/stores/useAuth';
	import { isApprove } from '@/utils';

	const authStore = useAuthStore()
</script>

<template>
	<Request :user="authStore?.user" v-if="authStore?.user?.skylight === 'req'"/>
	<Approve :user="authStore?.user" v-if="isApprove(authStore?.user?.skylight)"/>
	<Approve :user="authStore?.user" v-if="authStore?.user?.skylight === 'acct'"/>
</template>
