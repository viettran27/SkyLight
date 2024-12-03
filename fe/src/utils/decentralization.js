import { useAuthStore } from '@/stores/useAuth';
import { STATUS, POSITION } from '@/constants';

// EDIT REQUEST

const reqCanEditRequest = (user, department, status) => {
	return user?.skylight &&
	user?.skylight === POSITION.REQ &&
	(
		!status ||
		status === STATUS.HOD
	)
}

const acctCanEditRequest = (user, department, status) => {
	return user?.skylight &&
	user?.skylight === POSITION.ACCT &&
	department === user?.phongban &&
	status === STATUS.PENDING
}


export const canEditRequest = (status, ma_PR) => {
	if (!ma_PR) return;

	const authStore = useAuthStore();
	const department = ma_PR.split('_')[0];

	return (
		authStore.user?.skylight &&
		(
			reqCanEditRequest(authStore.user, department, status) ||
			acctCanEditRequest(authStore.user, department, status)
		)
	);
};

// EDIT DETAIL

const reqCanEditDetail = (user, department, status) => {
	return (
		(status === STATUS.HOD || status === STATUS.ACCT) &&
		user?.skylight === POSITION.REQ &&
		department === user?.phongban
	)
	||
	(
		(status === STATUS.ACCT || status === STATUS.ACCT_EDIT) &&
		user?.skylight === POSITION.ACCT &&
		department !== user?.phongban
	)
}

const acctCanEditDetail = (user, department, status) => {
	return status === STATUS.CA  &&
	user?.skylight === POSITION.ACCT &&
	department === user?.phongban
}

export const canEditDetail = (status, ma_PR) => {
	if (!status || !ma_PR) return;

	const authStore = useAuthStore();
	const department = ma_PR.split('_')[0];

	return (
		authStore.user?.skylight &&
		(
			reqCanEditDetail(authStore.user, department, status) ||
			acctCanEditDetail(authStore.user, department, status))
		);
};


export const statusApprove = (auth, status) => {
	const statusConfig = {
    [POSITION.REQ]: STATUS.ACCT_EDIT,
		[POSITION.HOD]: STATUS.HOD,
		[POSITION.ACCT]: STATUS.ACCT,
		[POSITION.CA]: STATUS.CA,
		[POSITION.DIR]: STATUS.DIR
	};

	return status === statusConfig[auth];
};

// ADD DETAIL

export const isAcctCanAdd = (pr, user) => {
  const phong_ban = pr?.split('_')[0];
	return user?.skylight === POSITION.ACCT && phong_ban === user?.phongban;
}

export const isReqCanAdd = (status, user) => {
  return (
    user?.skylight === POSITION.REQ &&
    (
      !status ||
      status === STATUS.HOD
    )
	);
}

export const canAddDetail = (status, pr, user) => {
  return isAcctCanAdd(pr, user) || isReqCanAdd(status, user)
}

// ORDERED

export const canOrdered = (auth, status) => {
	return auth === POSITION.ACCT && status === STATUS.DIR_ACPT
}
