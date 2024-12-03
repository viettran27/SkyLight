<script setup>
import { ref, reactive, watch, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '@/stores/useAuth';
import { useFilterStore } from '@/stores/useFilter';
import { useRouter } from 'vue-router';

import { axiosClient } from '@/lib/axios';
import { debounce } from 'lodash';
import { STATUS_APPROVE } from '@/constants';

import RequestHeader from '@/components/request/RequestHeader.vue';
import TableRequest from '@/components/request/TableRequest.vue';
import DialogRequest from '@/components/request/DialogRequest.vue';

const INIT_REQUEST = {
	Ten_PR: '',
	Muc_dich: '',
	Ngay_can: '',
};
const PER_PAGE = 10

const router = useRouter();

const dialog = reactive({
	open: false,
	status: 'add',
	value: INIT_REQUEST,
});
const pagination = reactive({
	page: 1,
	total: 0
})
const requests = ref([]);
const search = ref('');

const authStore = useAuthStore();
const filterStore = useFilterStore()

const getData = (page) => {
	axiosClient
		.get(`/requests?search=${search.value}&filter=${filterStore?.filter}&phong_ban=${authStore?.user?.phongban}&chuc_vu=${authStore?.user?.skylight}&page=${page || pagination.page}&per_page=${PER_PAGE}`)
		.then((data) => {
			requests.value = data.data;
			pagination.total = data.total
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

watch(() => filterStore.filter, () => {
	getData()
})

const handleSearch = (value) => {
	if (value) {
		axiosClient
			.get(`/requests?search=${value}&filter=${filterStore?.filter}&phong_ban=${authStore?.user?.phongban}&chuc_vu=${authStore?.user?.skylight}&page=${1}&per_page=${PER_PAGE}`)
			.then((data) => {
				requests.value = data.data;
				pagination.total = data.total
			});
	} else {
		getData();
	}
};

const handleDebouncedSearch = debounce((value) => {
	search.value = value
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

const handleChangePage = (page) => {
	getData(page)
}
</script>

<template>
	<div v-if="authStore?.user" class="flex flex-col h-full">
		<div class="pb-3">
			<h1 class="text-3xl">Yêu cầu</h1>
		</div>
		<RequestHeader
			:user="authStore?.user"
			@open-dialog="handleOpenDialog"
			@handle-search="handleDebouncedSearch"
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
			<Pagination 
				v-if="Math.ceil(pagination.total / PER_PAGE) > 1"
				class="flex justify-center mt-4" 
				v-slot="{ page }" 
				:total="pagination.total" 
				:itemsPerPage="PER_PAGE" 
				:sibling-count="1" 
				show-edges 
				:default-page="1"
				@update:page="handleChangePage"
			>
				<PaginationList v-slot="{ items }" class="flex items-center gap-1">
					<PaginationFirst />
					<PaginationPrev />

					<template v-for="(item, index) in items">
						<PaginationListItem v-if="item.type === 'page'" :key="index" :value="item.value" as-child>
							<Button class="w-10 h-10 p-0" :variant="item.value === page ? 'default' : 'outline'">
								{{ item.value }}
							</Button>
						</PaginationListItem>
						<PaginationEllipsis v-else :key="item.type" :index="index" />
					</template>

					<PaginationNext />
					<PaginationLast />
				</PaginationList>
			</Pagination>
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
