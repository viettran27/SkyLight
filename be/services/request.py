from typing import Optional
from db.base import get_db2
from sqlalchemy import func, and_, cast, Integer
from schemas.Request import M_Request
from enums.Auth import POSTITON
from enums.Request import STATUS
from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from datetime import datetime

class RequestService:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(phong_ban: str, chuc_vu: str) -> list[DB_Request]:
    db = get_db2()

    if chuc_vu == POSTITON.REQ.value or chuc_vu == POSTITON.HOD.value:
      all_requests = db.query(DB_Request).filter(DB_Request.Phong_ban == phong_ban).all()
    
    elif chuc_vu == POSTITON.ACCT.value:
      all_requests = db.query(DB_Request).filter(
        and_(
          DB_Request.Trang_thai != STATUS.HOD.value,
          DB_Request.Trang_thai != STATUS.HOD_RJ.value
        )
      ).all()
    
    else:
      all_requests = db.query(DB_Request).all()

    db.close()
    return all_requests

  @staticmethod
  def get_requests_with_pr(ma_pr: str) -> list[DB_Request]:
    db = get_db2()
    all_requests = db.query(DB_Request).filter(func.lower(DB_Request.Ma_PR).like(f"%{ma_pr.lower()}%")).all()
    db.close()
    return all_requests

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
      Trang_thai=STATUS.HOD.value if POSTITON.REQ.value == data.Chuc_vu else STATUS.CA.value,
      Thoi_gian_yeu_cau=datetime.now(),
    )

    db.add(new_request)
    db.commit()
    db.refresh(new_request)
    db.close()
    return new_request
  
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
  def approve(status: str, ma_pr: str):
    db = get_db2()

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status})

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