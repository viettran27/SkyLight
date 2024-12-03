<script setup>
import { ref, reactive, toRaw, toValue, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '@/stores/useAuth';

import { useRoute } from 'vue-router';
import { axiosClient } from '@/lib/axios';
import { debounce } from 'lodash';
import { STATUS_APPROVE } from '@/constants';

import { ChevronRight } from 'lucide-vue-next';
import DetailHeader from '@/components/detail/DetailHeader.vue';
import DialogDetail from '@/components/detail/DialogDetail.vue';
import TableDetail from '@/components/detail/TableDetail.vue';

const INIT_DIALOG = {
	Ma_vat_tu: '',
	Don_vi: '',
	Mo_ta: '',
	So_luong: 1,
	Don_gia: 0,
	Nha_cung_cap: '',
	Ngay_ve_du_kien: '',
};

const details = ref([]);
const status = ref(null);
const dialog = reactive({
	open: false,
	status: 'add',
	value: INIT_DIALOG,
});

const authStore = useAuthStore();
const route = useRoute();

const id_pr = route.params.id;

const getData = () => {
	axiosClient.get(`/request_details?ma_pr=${id_pr}`).then((data) => {
    status.value = data.status;
		details.value = data.data;
	});
};

onMounted(() => {
	getData();
});

const handleSearch = (value) => {
	if (value) {
		axiosClient
			.get(`/request_details/search?ma_pr=${id_pr}&ma_vat_tu=${value}`)
			.then((data) => {
				details.value = data;
			});
	} else {
		getData();
	}
};

const handleDebouncedSearch = debounce((value) => {
	handleSearch(value);
}, 300);

const emits = defineEmits(['getData', 'handleSearch']);

const handleAddDetail = () => {
	dialog.open = true;
	dialog.status = 'add';
	dialog.value = structuredClone(INIT_DIALOG);
};

const handleEdit = (material) => {
	dialog.open = true;
	dialog.status = 'update';
	dialog.value = structuredClone(toRaw(material));
};

const handleViewDetail = (material) => {
	dialog.open = true;
	dialog.status = 'view';
	dialog.value = structuredClone(toRaw(material));
};

const handleSaveDialog = async () => {
	const value = {
		Ma_PR: id_pr,
		Chuc_vu: authStore?.user?.skylight,
		...Object.fromEntries(
			Object.entries(toValue(dialog.value)).filter(
				([key, value]) => value,
			),
		),
	};
	switch (dialog.status) {
		case 'update':
			await axiosClient.put(`/request_details/${value.ID}`, value);
			break;

		default:
			await axiosClient.post('/request_details', value);
			break;
	}

	getData();
	dialog.open = false;
};

const handleApprove = () => {
	const data = {
		Status: STATUS_APPROVE.APPROVED,
		Ma_PR: id_pr,
		Auth: authStore?.user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		getData();
	});
};

const handleReject = () => {
	const data = {
		Status: STATUS_APPROVE.REJECTED,
		Ma_PR: id_pr,
		Auth: authStore?.user?.skylight,
	};

	axiosClient.post('/requests/approve', data).then(() => {
		getData();
	});
};

onBeforeUnmount(() => {
	handleDebouncedSearch.cancel();
});
</script>

<template>
	<div v-if="authStore?.user" class="flex flex-col h-full">
		<div class="flex items-end gap-2 pb-3">
			<router-link to="/requests">
				<h1>Yêu cầu</h1>
			</router-link>
			<ChevronRight />
			<h1>{{ id_pr }}</h1>
		</div>
		<DetailHeader
      :status="status"
      :id_pr="id_pr"
      :user="authStore?.user"
      @add-detail="handleAddDetail"
			@handle-search="handleDebouncedSearch"
      @approve="handleApprove"
      @reject="handleReject"
		/>
		<div class="bg-white flex-1 pb-3 overflow-auto">
			<TableDetail
				:value="details"
				:id_pr="id_pr"
				@edit-detail="handleEdit"
				@view-detail="handleViewDetail"
				@get-data="getData"
			/>
		</div>
	</div>
	<DialogDetail
		:value="dialog.value"
		:status="dialog.status"
		:open-dialog="dialog.open"
		:isAcct="authStore?.user?.skylight === 'acct'"
		@handle-save="handleSaveDialog"
		@handle-close="() => (dialog.open = false)"
	/>
</template>
