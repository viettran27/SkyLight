from pydantic import BaseModel
from datetime import date, datetime

class M_Request(BaseModel):
  Ma_PR: str
  Phong_ban: str
  Ten_PR: str
  Muc_dich: str
  Ngay_can: date
  Nguoi_yeu_cau: str
  Thoi_gian_yeu_cau: datetime

class M_Request_Info(M_Request):
  Truong_BP_duyet: datetime
  Ke_toan_phe_duyet: datetime
  BLD_phe_duyet: datetime
  Thoi_diem_dat_hang: datetime
  Thoi_diem_ve_kho: datetime
  Trang_thai: str
  Ghi_chu: str
