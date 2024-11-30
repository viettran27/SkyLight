from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS, STATUS_APPROVE
from datetime import datetime

class HOD:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(phong_ban: str):
    db = get_db2()
    
    result = db.query(DB_Request).filter(
      and_(
        DB_Request.Phong_ban == phong_ban,
        DB_Request.Trang_thai.isnot(None)
      )
    ).all()

    db.close()
    return result
  
  @staticmethod
  def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()

    status_text = STATUS.HOD_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.ACCT.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.Truong_BP_duyet: datetime.now()})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})
    
    db.commit()
    db.close()
    return result
