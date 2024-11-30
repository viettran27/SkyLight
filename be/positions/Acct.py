from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS, STATUS_APPROVE
from datetime import datetime

class ACCT:
  def __init__(self):
    pass

  @staticmethod
  def get_requests():
    db = get_db2()
    
    result = db.query(DB_Request).filter(
      and_(
        DB_Request.Trang_thai != STATUS.HOD.value,
        DB_Request.Trang_thai != STATUS.HOD_RJ.value
      )
    ).all()

    db.close()
    return result
  
  @staticmethod
  def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()

    status_text = STATUS.ACCT_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.CA.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.Ke_toan_phe_duyet: datetime.now()})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})
    
    db.commit()
    db.close()
    return result
