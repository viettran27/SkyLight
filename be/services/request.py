from typing import Optional
from db.base import get_db
from schemas.Request import M_Request
from models.Request import DB_Request
from datetime import datetime

class RequestService:
  def __init__(self):
    pass

  @staticmethod
  def get_requests() -> list[DB_Request]:
    db = get_db()
    return db.query(DB_Request).all()

  @staticmethod
  def create_request(data: M_Request) -> Optional[DB_Request]:
    db = get_db()

    new_request = DB_Request(
      Ma_PR=data.Ma_PR,
      Phong_ban=data.Phong_ban,
      Ten_PR=data.Ten_PR,
      Muc_dich=data.Muc_dich,
      Ngay_can=data.Ngay_can,
      Nguoi_yeu_cau=data.Nguoi_yeu_cau,
      Thoi_gian_yeu_cau=datetime.now(),
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    return new_request
  
  @staticmethod
  def update_request(data: M_Request) -> Optional[DB_Request]:
    db = get_db()
    db.query(DB_Request).filter(DB_Request.Ma_PR == data.Ma_PR).update({
      DB_Request.Phong_ban: data.Phong_ban,
      DB_Request.Ten_PR: data.Ten_PR,
      DB_Request.Muc_dich: data.Muc_dich,
      DB_Request.Ngay_can: data.Ngay_can,
      DB_Request.Nguoi_yeu_cau: data.Nguoi_yeu_cau,
      DB_Request.Thoi_gian_yeu_cau: datetime.now(),
    })
    db.commit()
    return db.query(DB_Request).filter(DB_Request.Ma_PR == data.Ma_PR).first()
  
  @staticmethod
  def delete_request(ma_pr: str) -> int:
    db = get_db()
    
    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).delete()
    db.commit()

    return result
  