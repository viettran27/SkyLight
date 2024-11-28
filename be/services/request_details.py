from typing import Optional
from db.base import get_db
from schemas.RequestDetail import M_Request_Req, M_Request_Not_Req
from models.RequestDetail import DB_Request_Detail
from datetime import datetime

class RequestDetailService:

  def __init__(self):
    pass

  @staticmethod
  def get_requests(ma_pr: str) -> list[DB_Request_Detail]:
    db = get_db()
    return db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).all()

  @staticmethod
  def create_request(data: M_Request_Req | M_Request_Not_Req) -> Optional[DB_Request_Detail]:
    db= get_db()

    new_request_detail = DB_Request_Detail(
      Ma_PR=data.Ma_PR,
      Ma_vat_tu=data.Ma_vat_tu,
      Mo_ta=data.Mo_ta,
      Don_vi=data.Don_vi,
      So_luong=data.So_luong,
      Trang_thai="Đang đợi duyệt",
      Thoi_gian_yeu_cau=datetime.now(),
    )

    db.add(new_request_detail)
    db.commit()
    db.refresh(new_request_detail)

    return new_request_detail
  
  @staticmethod
  def update_request(id: int, data: M_Request_Req | M_Request_Not_Req) -> Optional[DB_Request_Detail]:
    db= get_db()

    db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).update({
      DB_Request_Detail.Ma_vat_tu: data.Ma_vat_tu,
      DB_Request_Detail.Mo_ta: data.Mo_ta,
      DB_Request_Detail.Don_vi: data.Don_vi,
      DB_Request_Detail.So_luong: data.So_luong,
    })

    db.commit()
    return db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).first()
  
  @staticmethod
  def delete_request(id: int) -> int:
    db = get_db()
    
    result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).delete()
    db.commit()

    return result