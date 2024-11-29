from typing import Optional
from db.base import get_db2
from sqlalchemy import func
from schemas.RequestDetail import M_Request_Req, M_Request_Req_Update
from models.RequestDetail import DB_Request_Detail
from datetime import datetime

class RequestDetailService:

  def __init__(self):
    pass

  @staticmethod
  def get_requests(ma_pr: str) -> list[DB_Request_Detail]:
    db = get_db2()
    all_details = db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).all()
    db.close()
    return all_details
  
  @staticmethod
  def get_requests_with_vt(ma_pr:str, ma_vat_tu: str) -> list[DB_Request_Detail]:
    db = get_db2()
    all_details = db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr, func.lower(DB_Request_Detail.Ma_vat_tu).like(f"%{ma_vat_tu.lower()}%")).all()
    db.close()
    return all_details

  @staticmethod
  def create_request(data: M_Request_Req) -> Optional[DB_Request_Detail]:
    db= get_db2()

    new_request_detail = DB_Request_Detail(
      Ma_PR=data.Ma_PR,
      Ma_vat_tu=data.Ma_vat_tu,
      Mo_ta=data.Mo_ta,
      Don_vi=data.Don_vi,
      So_luong=data.So_luong,
      Trang_thai="Đang đợi trưởng bộ phận duyệt",
      Thoi_gian_yeu_cau=datetime.now(),
    )

    db.add(new_request_detail)
    db.commit()
    db.refresh(new_request_detail)
    db.close()
    return new_request_detail
  
  @staticmethod
  def update_request(id: int, data: M_Request_Req_Update) -> Optional[DB_Request_Detail]:
    db= get_db2()

    result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).update({
      DB_Request_Detail.Ma_vat_tu: data.Ma_vat_tu,
      DB_Request_Detail.Mo_ta: data.Mo_ta,
      DB_Request_Detail.Don_vi: data.Don_vi,
      DB_Request_Detail.So_luong: data.So_luong,
    })
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def delete_request(id: int) -> int:
    db = get_db2()
    result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).delete()
    db.commit()
    db.close()
    return result