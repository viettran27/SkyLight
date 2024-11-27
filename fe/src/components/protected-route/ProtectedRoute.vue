<template>
	<div v-if="true">
		<router-view />
	</div>
</template>

<script setup>
import { useRouter } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/useAuth';

const router = useRouter();
const isAuthenticated = ref(false);

onMounted(() => {
	const authStore = useAuthStore();
	isAuthenticated.value = !!authStore.accessToken;
	authStore.getMe();

	if (!isAuthenticated.value) {
		router.push('/login');
	}
});
</script>
