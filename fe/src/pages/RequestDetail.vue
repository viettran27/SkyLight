<script setup>
import { ref, reactive, toRaw, toValue, onMounted, onBeforeUnmount } from 'vue';
import { useAuthStore } from '@/stores/useAuth';

import { useRoute } from 'vue-router';
import { axiosClient } from '@/lib/axios';
import { debounce } from 'lodash';
import { isApprove } from '@/utils';

import { ChevronRight } from 'lucide-vue-next';
import ApproveDetail from '@/components/decentralization/ApproveDetail.vue';
import RequestDetail from '@/components/decentralization/RequestDetail.vue';
import AccountantDetail from '@/components/decentralization/AccountantDetail.vue';
import DialogDetail from '@/components/ui-custom/DialogDetail.vue';

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
		details.value = data;
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
			await axiosClient.post('/request_details', data);
			break;
	}

	getData();
	dialog.open = false;
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
		<RequestDetail
			:id_pr="id_pr"
			:details="details"
			:user="authStore?.user"
			@get-data="getData"
			@handle-search="handleDebouncedSearch"
			v-if="authStore?.user?.skylight === 'req'"
		/>
		<ApproveDetail
			:id_pr="id_pr"
			:details="details"
			:user="authStore?.user"
			@get-data="getData"
			@handle-search="handleDebouncedSearch"
			v-if="
				isApprove(authStore?.user?.skylight) &&
				authStore?.user?.skylight !== 'acct'
			"
		/>
		<AccountantDetail
			:id_pr="id_pr"
			:details="details"
			:user="authStore?.user"
			@get-data="getData"
			@handle-search="handleDebouncedSearch"
			v-if="authStore?.user?.skylight === 'acct'"
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
