<script setup>
	import { AlignJustify, Bell } from 'lucide-vue-next';
	import { useAuthStore } from '@/stores/useAuth';
	import { useRouter } from 'vue-router'

	const authStore = useAuthStore()
	const router = useRouter()
	const logout = () => {
		authStore.logout();	
		router.push("/login")
	}
</script>

<template>
	<header class="h-[60px] border-b border-gray-300 bg-white">
		<div class="flex justify-between items-center px-4 h-full">
			<AlignJustify class="cursor-pointer" />
			<div class="flex gap-2 items-center">
				<Bell />
				<DropdownMenu>
					<DropdownMenuTrigger>
						<div
							class="bg-gray-300 rounded-full w-8 h-8 cursor-pointer"
						></div>
					</DropdownMenuTrigger>
					<DropdownMenuContent>
						<DropdownMenuItem @click="logout">Đăng xuất</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			</div>
		</div>
	</header>
</template>
