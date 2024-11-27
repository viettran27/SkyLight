<script setup>
import { AlignJustify, Bell } from 'lucide-vue-next';
</script>

<template>
	<header class="h-[60px] border-b border-gray-300">
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
						<DropdownMenuItem>Đăng xuất</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
			</div>
		</div>
	</header>
</template>
