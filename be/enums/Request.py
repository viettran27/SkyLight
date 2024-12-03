from enum import Enum

class STATUS_APPROVE(Enum):
  APPROVED = "APPROVED"
  REJECTED = "REJECTED"

class STATUS(Enum):
  HOD = "Đang đợi trưởng bộ phận duyệt"
  ACCT = "Trưởng bộ phận đã duyệt"
  CA = "Kế toán đã duyệt"
  DIR = "Kế toán trưởng đã duyệt"
  DIR_ACPT = "Đã duyệt"
  HOD_RJ = "Trưởng bộ phận từ chối"
  ACCT_RJ = "Kế toán từ chối"
  CA_RJ = "Kế toán trưởng từ chối"
  DIR_RJ = "Lãnh đạo từ chối"
  ACCT_EDIT = "Kế toán đã chỉnh sửa"
  REQ_ACPT = "Người yêu cầu và kế toán đã duyệt"
  REQ_RJ = "Người yêu cầu từ chối sửa"
  ACCT_ORDERED = "Kế toán đã đặt hàng"

class FILTER(Enum):
  ALL = "all"
  NOT_APPROVE = "not_approve"
  APPROVED = "approved"
  HOD = STATUS.HOD.value
  ACCT = STATUS.ACCT.value
  CA = STATUS.CA.value
  DIR = STATUS.DIR.value
  DIR_ACCEPT = STATUS.DIR_ACPT.value