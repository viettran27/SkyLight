export const STATUS_APPROVE = {
	APPROVED: 'APPROVED',
	REJECTED: 'REJECTED',
};

export const STATUS = {
	HOD: "Đang đợi trưởng bộ phận duyệt",
  ACCT: "Trưởng bộ phận đã duyệt",
  CA: "Kế toán đã duyệt",
  DIR: "Kế toán trưởng đã duyệt",
	DIR_ACPT: 'Đã duyệt',
	HOD_RJ: 'Trưởng bộ phận từ chối',
	ACCT_RJ: 'Kế toán từ chối',
	CA_RJ: 'Kế toán trưởng từ chối',
	DIR_RJ: 'Lãnh đạo từ chối',
	ACCT_EDIT: 'Kế toán đã chỉnh sửa',
	REQ_ACPT: 'Người yêu cầu và kế toán đã duyệt',
	REQ_RJ: 'Người yêu cầu từ chối sửa',
	ACCT_ORDERED: 'Kế toán đã đặt hàng'
};

export const FILTER = {
  ALL: "all",
  NOT_APPROVE: "not_approve",
  APPROVED: "approved",
  HOD: STATUS.HOD,
  ACCT: STATUS.ACCT,
  CA: STATUS.CA,
  DIR: STATUS.DIR,
	DIR_ACCEPT: STATUS.DIR_ACPT
}
