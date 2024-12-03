from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS, STATUS_APPROVE, FILTER
from datetime import datetime

class ACCT:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(filter: FILTER = None):
    db = get_db2()

    filters = {
      FILTER.ALL: [
          DB_Request.Trang_thai != STATUS.HOD.value,
          DB_Request.Trang_thai != STATUS.HOD_RJ.value,
      ],
      FILTER.APPROVED: [
          DB_Request.Trang_thai != STATUS.HOD.value,
          DB_Request.Trang_thai != STATUS.ACCT.value,
      ],
      FILTER.NOT_APPROVE: [
          DB_Request.Trang_thai == STATUS.ACCT.value,
      ],
    }

    filter_conditions = filters.get(filter, [DB_Request.Trang_thai == filter.value])
    result = db.query(DB_Request).filter(and_(*filter_conditions)).all()

    db.close()
    return result
  
  @staticmethod
  async def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()
    status_pr = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).first().Trang_thai

    if status_pr == STATUS.DIR_ACPT.value:
      status_text = STATUS.ACCT_ORDERED.value
      result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text})
    else:
      status_text = STATUS.ACCT_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.CA.value
      result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.Ke_toan_phe_duyet: datetime.now()})
    
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})
    
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def get_notification():
    db = get_db2()
    acct_accept = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.ACCT.value).all()
    acct_ordered = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.DIR_ACPT.value).all()

    return {
      "acct_accept": len(acct_accept),
      "acct_ordered": len(acct_ordered)
    }
