<script setup>
import Navbar from './Navbar.vue';
import Header from './Header.vue';
</script>

<template>
	<div class="flex">
		<Navbar />
		<div class="h-[100vh] flex-1">
			<Header />
			<div class="bg-gray-200 h-[calc(100vh-60px)] w-full p-3 px-5">
				<router-view />
			</div>
		</div>
	</div>
</template>
