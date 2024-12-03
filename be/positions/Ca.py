from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import or_
from enums.Request import STATUS, STATUS_APPROVE, FILTER
from datetime import datetime

class CA:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(filter: FILTER = None):
    db = get_db2()
    
    filters = {
      FILTER.ALL: [
        DB_Request.Trang_thai == STATUS.CA.value,
        DB_Request.Trang_thai == STATUS.CA_RJ.value,
        DB_Request.Trang_thai == STATUS.REQ_ACPT.value,
        DB_Request.Trang_thai == STATUS.DIR.value,
        DB_Request.Trang_thai == STATUS.ACCT_ORDERED.value
      ],
      FILTER.APPROVED: [
        DB_Request.Trang_thai == STATUS.DIR.value,
        DB_Request.Trang_thai == STATUS.DIR_ACPT.value,
        DB_Request.Trang_thai == STATUS.DIR_RJ.value,
        DB_Request.Trang_thai == STATUS.ACCT_ORDERED.value
      ],
      FILTER.NOT_APPROVE: [
        DB_Request.Trang_thai == STATUS.CA.value,
      ],
    }

    filter_conditions = filters.get(filter, [DB_Request.Trang_thai == filter.value])
    result = db.query(DB_Request).filter(or_(*filter_conditions)).all()

    db.close()
    return result
  
  @staticmethod
  async def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()

    status_text = STATUS.CA_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.DIR.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.Ke_toan_phe_duyet: datetime.now()})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})

    db.commit()
    db.close()
    return result

  @staticmethod
  def get_notification():
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.CA.value).all()
    db.close()
    
    return {
      "ca_accept": len(result)
    }