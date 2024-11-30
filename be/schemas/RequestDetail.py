from pydantic import BaseModel
from datetime import date

class M_Request_Detail(BaseModel):
  Ma_PR: str
  Chuc_vu: str
  Ma_vat_tu: str
  Mo_ta: str
  Don_vi: str
  So_luong: int
  Don_gia: int = None
  Nha_cung_cap: str = None
  Ngay_ve_du_kien: date  = None



