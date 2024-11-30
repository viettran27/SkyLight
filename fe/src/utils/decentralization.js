import { useAuthStore } from '@/stores/useAuth';
import { STATUS, POSITION } from '@/constants';

export const canEditRequest = (status, ma_PR) => {
	if (!status || !ma_PR) return;

	const authStore = useAuthStore();
	const department = ma_PR.split('_')[0];

	return (
		(authStore.user?.skylight &&
			(status === STATUS.HOD || status === STATUS.ACCT) &&
			authStore.user?.skylight === POSITION.REQ &&
			department === authStore.user?.phongban) ||
		(status === STATUS.CA &&
			authStore.user?.skylight === POSITION.CA &&
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
			authStore.user?.skylight === POSITION.REQ &&
			department === authStore.user?.phongban) ||
		((status === STATUS.ACCT || status === STATUS.ACCT_EDIT) &&
			authStore.user?.skylight === POSITION.ACCT &&
			department !== authStore.user?.phongban) ||
		(status === STATUS.CA &&
			authStore.user?.skylight === POSITION.ACCT &&
			department === authStore.user?.phongban)
	);
};

export const isApprove = (auth) => {
	return (
		auth === POSITION.HOD ||
		auth === POSITION.ACCT ||
		auth === POSITION.CA ||
		auth === POSITION.DIR
	);
};

export const statusFit = (auth) => {
	const status = {
		[POSITION.HOD]: STATUS.HOD,
		[POSITION.ACCT]: STATUS.ACCT,
		[POSITION.CA]: STATUS.CA,
		[POSITION.DIR]: STATUS.DIR,
	};

	return status[auth];
};
