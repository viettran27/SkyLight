<script setup>
import { ref } from 'vue';
import Navbar from './Navbar.vue';
import Header from './Header.vue';

const openNavbar = ref(false);

const toggleNavbar = () => {
	openNavbar.value = !openNavbar.value;
};
</script>

<template>
	<div class="flex overflow-hidden">
		<Navbar :openNavbar="openNavbar" />
		<div class="h-[100vh] flex-1 w-[calc(100%-250px)] bg-gray-200">
			<Header @toggleNavbar="toggleNavbar" />
			<div class="h-[calc(100vh-60px)] w-full p-3 px-5">
				<router-view />
			</div>
		</div>
	</div>
</template>
