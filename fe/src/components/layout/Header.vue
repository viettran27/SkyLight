<script setup>
import { onMounted, onBeforeUnmount, watch, computed } from 'vue'
import { AlignJustify, Bell } from 'lucide-vue-next';

import { useAuthStore } from '@/stores/useAuth';
import { useRouter } from 'vue-router';
import { useWebSocketStore } from "@/stores/useWebSocket";
import { useFilterStore } from '@/stores/useFilter';

import { FILTER } from '@/constants';

const authStore = useAuthStore();
const webSocketStore = useWebSocketStore();
const filterStore = useFilterStore();
const router = useRouter();

const emit = defineEmits(["toggleNavbar"])

const logout = () => {
	authStore.logout();
	filterStore.reset()
	router.push('/login');
};

onMounted(() => {
	webSocketStore.connect();
});

onBeforeUnmount(() => {
	webSocketStore.disconnect();
});

const handleRedirectFilter = (filter) => {
	filterStore.setFilter(filter);
	router.push('/requests');
}

const countNotification = computed(() => {
	return Object.keys(webSocketStore.notifications).reduce((total, key) => total + webSocketStore.notifications[key], 0);
})

</script>

<template>
	<header class="h-[60px] border-b border-gray-300 bg-white">
		<div class="flex justify-between items-center px-4 h-full">
			<AlignJustify class="cursor-pointer" @click="$emit('toggleNavbar')"/>
			<div class="flex gap-4 items-center">
				<DropdownMenu>
					<DropdownMenuTrigger>
						<div class="relative">
							<Bell />
							<span v-if="countNotification > 0" class="absolute bg-red-500 text-white rounded-full w-4 h-4 text-xs flex items-center justify-center -top-[5px] right-[-5px]">{{countNotification}}</span>
						</div>
					</DropdownMenuTrigger>
					<DropdownMenuContent v-if="countNotification > 0">
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.hod_accept">Bạn có {{webSocketStore.notifications?.hod_accept}} yêu cầu đang đợi duyệt</DropdownMenuItem>
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.acct_accept">Bạn có {{webSocketStore.notifications?.acct_accept}} yêu cầu đang đợi duyệt</DropdownMenuItem>
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.acct_ordered">Bạn có {{webSocketStore.notifications?.acct_ordered}} yêu cầu cần mua</DropdownMenuItem>
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.ca_accept">Bạn có {{webSocketStore.notifications?.ca_accept}} yêu cầu cần duyệt</DropdownMenuItem>
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.dir_accept">Bạn có {{webSocketStore.notifications?.dir_accept}} yêu cầu cần duyệt</DropdownMenuItem>
						<DropdownMenuItem @click="handleRedirectFilter(FILTER.NOT_APPROVE)" v-if="webSocketStore.notifications?.req_edit">Bạn có {{webSocketStore.notifications?.req_edit}} yêu cầu mà thư ký đã sửa</DropdownMenuItem>
					</DropdownMenuContent>
				</DropdownMenu>
				<div class="flex gap-2 items-center">
					<DropdownMenu>
						<DropdownMenuTrigger>
							<div
								class="bg-gray-300 rounded-full w-8 h-8 cursor-pointer"
							></div>
						</DropdownMenuTrigger>
						<DropdownMenuContent>
							<DropdownMenuItem @click="logout"
								>Đăng xuất</DropdownMenuItem
							>
						</DropdownMenuContent>
					</DropdownMenu>
					<span>{{ authStore?.user?.hoten }}</span>
				</div>
			</div>
		</div>
	</header>
</template>
