import { useAuthStore } from '@/stores/useAuth';
import { STATUS, POSTITON } from '@/constants';

export const canEditRequest = (status, ma_PR) => {
	if (!status || !ma_PR) return;

	const authStore = useAuthStore();
	const department = ma_PR.split('_')[0];

	return (
		(authStore.user?.skylight &&
			(status === STATUS.HOD || status === STATUS.ACCT) &&
			authStore.user?.skylight === POSTITON.REQ &&
			department === authStore.user?.phongban) ||
		(status === STATUS.CA &&
			authStore.user?.skylight === POSTITON.CA &&
			department === authStore.user?.phongban)
	);
};

export const canEditDetail = (status, ma_PR) => {
	if (!status || !ma_PR) return;

	const authStore = useAuthStore();
	const department = ma_PR.split('_')[0];

	return (
		(authStore.user?.skylight &&
			(status === STATUS.HOD || status === STATUS.ACCT) &&
			authStore.user?.skylight === POSTITON.REQ &&
			department === authStore.user?.phongban) ||
		((status === STATUS.ACCT || status === STATUS.ACCT_EDIT) &&
			authStore.user?.skylight === POSTITON.ACCT &&
			department !== authStore.user?.phongban) ||
		(status === STATUS.CA &&
			authStore.user?.skylight === POSTITON.ACCT &&
			department === authStore.user?.phongban)
	);
};

export const isApprove = (auth) => {
	return (
		auth === POSTITON.HOD ||
		auth === POSTITON.ACCT ||
		auth === POSTITON.CA ||
		auth === POSTITON.DIR
	);
};

export const statusFit = (auth) => {
	const status = {
		[POSTITON.HOD]: STATUS.HOD,
		[POSTITON.ACCT]: STATUS.ACCT,
		[POSTITON.CA]: STATUS.CA,
		[POSTITON.DIR]: STATUS.DIR,
	};

	return status[auth];
};
