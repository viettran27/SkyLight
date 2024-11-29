from pydantic import BaseModel

class M_Request_Req(BaseModel):
  Ma_PR: str
  Ma_vat_tu: str
  Mo_ta: str
  Don_vi: str
  So_luong: int

class M_Request_Req_Update(BaseModel):
  Ma_vat_tu: str
  Mo_ta: str
  Don_vi: str
  So_luong: int

class M_Request_Not_Req(BaseModel):
  Don_gia: str
  Thanh_tien: int
  Nha_cung_cap: str
  Ghi_chu: str

