<script setup>
import { ref, reactive, watch, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '@/stores/useAuth';
import { useRouter } from 'vue-router';

import { axiosClient } from '@/lib/axios';
import { debounce } from 'lodash';
import { isApprove } from '@/utils';
import { STATUS_APPROVE } from '@/constants';

import Request from '@/components/decentralization/Request.vue';
import Approve from '@/components/decentralization/Approve.vue';
import TableRequest from '@/components/ui-custom/TableRequest.vue';
import DialogRequest from '@/components/ui-custom/DialogRequest.vue';

const INIT_REQUEST = {
	Ten_PR: '',
	Muc_dich: '',
	Ngay_can: '',
};

const router = useRouter();

const dialog = reactive({
	open: false,
	status: 'add',
	value: INIT_REQUEST,
});
const requests = ref([]);
const authStore = useAuthStore();

const getData = () => {
	axiosClient
		.get(
			`/requests?phong_ban=${authStore?.user?.phongban}&chuc_vu=${authStore?.user?.skylight}`,
		)
		.then((data) => {
			requests.value = data;
		});
};

onMounted(() => {
	if (authStore.user) getData();
});

onBeforeUnmount(() => {
	handleDebouncedSearch.cancel();
});

watch([authStore], () => {
	if (authStore.user) getData();
});

const handleSearch = (value) => {
	if (value) {
		axiosClient.get(`/requests/search?ma_pr=${value}`).then((data) => {
			requests.value = data;
		});
	} else {
		getData();
	}
};

const handleDebouncedSearch = debounce((value) => {
	handleSearch(value);
}, 300);

const handleOpenDialog = () => {
	dialog.open = true;
	dialog.status = 'add';
	dialog.value = INIT_REQUEST;
};

const handleCloseDialog = () => {
	dialog.open = false;
	dialog.value = INIT_REQUEST;
};

const handleSaveDialog = () => {
	const data = {
		Chuc_vu: authStore?.user?.skylight,
		Ten_PR: dialog.value.Ten_PR,
		Muc_dich: dialog.value.Muc_dich,
		Ngay_can: dialog.value.Ngay_can,
		Phong_ban: authStore?.user.phongban,
		Nguoi_yeu_cau: authStore?.user.hoten,
	};

	switch (dialog.status) {
		case 'update':
			axiosClient
				.put(`/requests/${dialog.value.Ma_PR}`, data)
				.then(() => {
					dialog.open = false;
					getData();
				});
			break;

		default:
			axiosClient.post('/requests', data).then((request) => {
				router.push(`/requests/${request.Ma_PR}`);
			});
			break;
	}
};

const handleUpdateRequest = (request) => {
	dialog.open = true;
	dialog.status = 'update';
	dialog.value = request;
};

const handleDeleteRequest = (ma_pr) => {
	axiosClient.delete(`/requests/${ma_pr}`).then(() => {
		getData();
	});
};

const handleApprove = (ma_pr) => {
	const data = {
		Status: STATUS_APPROVE.APPROVED,
		Ma_PR: ma_pr,
		Auth: authStore?.user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		getData();
	});
};

const handleReject = (ma_pr) => {
	const data = {
		Status: STATUS_APPROVE.REJECTED,
		Ma_PR: ma_pr,
		Auth: authStore?.user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		getData();
	});
};
</script>

<template>
	<div v-if="authStore?.user" class="flex flex-col h-full">
		<div class="pb-3">
			<h1 class="text-3xl">Yêu cầu</h1>
		</div>
		<Request
			:user="authStore?.user"
			:requests="requests"
			@open-dialog="handleOpenDialog"
			@handle-search="handleDebouncedSearch"
			v-if="
				authStore?.user?.skylight === 'req' ||
				authStore?.user?.skylight === 'acct'
			"
		/>
		<Approve
			:user="authStore?.user"
			:requests="requests"
			@get-data="getData"
			@handle-search="handleDebouncedSearch"
			v-if="
				isApprove(authStore?.user?.skylight) &&
				authStore?.user?.skylight !== 'acct'
			"
		/>
		<div class="bg-white flex-1 pb-3 overflow-auto">
			<TableRequest
				:value="requests"
				:user="authStore?.user"
				@update-request="handleUpdateRequest"
				@delete-request="handleDeleteRequest"
				@approve="handleApprove"
				@reject="handleReject"
			/>
		</div>
		<DialogRequest
			:open="dialog.open"
			:status="dialog.status"
			:value="dialog.value"
			@close-dialog="handleCloseDialog"
			@save-dialog="handleSaveDialog"
		/>
	</div>
</template>
