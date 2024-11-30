from enum import Enum

class STATUS_APPROVE(Enum):
  APPROVED = "APPROVED"
  REJECTED = "REJECTED"

class STATUS(Enum):
  HOD = "Đang đợi trưởng bộ phận duyệt"
  ACCT = "Đang đợi kế toán duyệt"
  CA = "Đang đợi kế toán trưởng duyệt"
  DIR = "Đang đợi duyệt cuối cùng"
  DONE = "Đã duyệt"
  HOD_RJ = "Trưởng bộ phận từ chối"
  ACCT_RJ = "Kế toán từ chối"
  CA_RJ = "Kế toán trưởng từ chối"
  DIR_RJ = "Lãnh đạo từ chối"
  ACCT_EDIT = "Kế toán đã chỉnh sửa"
  REQ_ACPT = "Người yêu cầu chấp nhận sửa"
  REQ_RJ = "Người yêu cầu từ chối sửa"