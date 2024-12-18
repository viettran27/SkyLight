from typing import Optional
from db.base import get_db2
from sqlalchemy import func, cast, Integer
from schemas.Request import M_Request
from models.Request import DB_Request
from datetime import datetime

class RequestService:
  def __init__(self):
    pass

  @staticmethod
  def create_request(data: M_Request) -> Optional[DB_Request]:
    db = get_db2()

    max_ma_pr = db.query(
      func.max(
        cast(
          func.substring(DB_Request.Ma_PR, func.charindex('_', DB_Request.Ma_PR) + 1, 10), 
          Integer
        )
    )).filter(DB_Request.Phong_ban == data.Phong_ban).scalar()
    ma_pr = data.Phong_ban + "_" + str(int(max_ma_pr) + 1) if max_ma_pr else f'{data.Phong_ban}_1'

    new_request = DB_Request(
      Ma_PR=ma_pr,
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
    db.close()
    return new_request
  
  @staticmethod
  def get_request_by_pr(ma_pr: str) -> Optional[DB_Request]:
    db = get_db2()
    request = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).first()
    db.close()
    return request

  @staticmethod
  def update_request(ma_pr: str, data: M_Request) -> Optional[DB_Request]:
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({
      DB_Request.Phong_ban: data.Phong_ban,
      DB_Request.Ten_PR: data.Ten_PR,
      DB_Request.Muc_dich: data.Muc_dich,
      DB_Request.Ngay_can: data.Ngay_can,
      DB_Request.Nguoi_yeu_cau: data.Nguoi_yeu_cau,
      DB_Request.Thoi_gian_yeu_cau: datetime.now(),
    })
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def delete_request(ma_pr: str) -> int:
    db = get_db2()
    
    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).delete()
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def update_status(ma_pr: str, status: str):
    db = get_db2()

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status})

    db.commit()
    db.close()
    return result
  
  @staticmethod
  def update_status_when_create_detail(ma_pr: str, status: str):
    db = get_db2()

    request = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).first()
    if request.Trang_thai is None:
      db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status})

    db.commit()
    db.close()

  @staticmethod
  def update_total_thanh_tien(ma_pr:str, total: int):
    db = get_db2()
    db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Tong_so_tien: total})
    db.commit()
    db.close()