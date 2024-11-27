<script setup>
import { watch, ref } from 'vue';
import { cn } from '@/lib/utils';
import { useRoute } from 'vue-router';
import { Package, HandCoins, Wallet, ChevronDown } from 'lucide-vue-next';

const route = useRoute();
const currentPath = ref(route.path);

watch(
	() => route.path,
	() => {
		currentPath.value = route.path;
	},
);

const navbar = [
	{
		type: 'collapse',
		icon: Package,
		name: 'Vật liệu',
		children: [
			{
				href: '/requests',
				name: 'Yêu cầu',
			},
			{
				href: '/responses',
				name: 'Phản hồi',
			},
		],
	},
	{
		type: 'single',
		icon: HandCoins,
		href: '/automatic_salary',
		name: 'Tính lương tự động',
	},
	{
		type: 'single',
		icon: Wallet,
		href: '/manage_wallet',
		name: 'Quản lý tài sản',
	},
];
</script>
<template>
	<div class="h-[100vh] min-w-[250px] border-r border-gray-300">
		<div class="min-h-[60px] flex justify-center items-center">
			<h1 class="text-primary text-3xl font-bold">SKYLIGHT</h1>
		</div>
		<div class="px-3 py-3 mt-3">
			<div v-for="(item, index) in navbar" :key="index" class="menu">
				<div v-if="item.type === 'collapse'">
					<Collapsible>
						<CollapsibleTrigger
							class="flex justify-between items-center w-full px-4"
						>
							<div class="flex gap-2 py-3">
								<component :is="item.icon" />
								<span>{{ item.name }}</span>
							</div>
							<ChevronDown />
						</CollapsibleTrigger>
						<CollapsibleContent class="ml-12">
							<ul class="border-l border-gray-300 my-2">
								<li
									v-for="(child, index) in item.children"
									:key="index"
									:class="
										cn(
											currentPath === child.href &&
												'bg-gray-300',
											'py-2 px-4 ml-2 mr-4 rounded-lg',
										)
									"
								>
									<router-link
										:to="child.href"
										class="w-full block"
									>
										{{ child.name }}
									</router-link>
								</li>
							</ul>
						</CollapsibleContent>
					</Collapsible>
				</div>
				<div v-else>
					<router-link :to="item.href">
						<div
							:class="
								cn(
									currentPath === item.href && 'bg-gray-300',
									'flex gap-2 py-3 px-4 w-full cursor-pointer rounded-lg',
								)
							"
						>
							<component :is="item.icon" />
							<span>{{ item.name }}</span>
						</div>
					</router-link>
				</div>
			</div>
		</div>
	</div>
</template>
