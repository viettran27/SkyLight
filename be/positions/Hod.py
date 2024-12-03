from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS, STATUS_APPROVE, FILTER
from datetime import datetime

class HOD:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(phong_ban: str, filter: FILTER = None):
    db = get_db2()
    
    filters = {
        FILTER.ALL: [
            DB_Request.Phong_ban == phong_ban,
            DB_Request.Trang_thai.isnot(None),
        ],
        FILTER.APPROVED: [
            DB_Request.Phong_ban == phong_ban,
            DB_Request.Trang_thai != STATUS.HOD.value,
        ],
        FILTER.NOT_APPROVE: [
            DB_Request.Phong_ban == phong_ban,
            DB_Request.Trang_thai == STATUS.HOD.value,
        ],
    }

    default_condition = [
      DB_Request.Phong_ban == phong_ban,
      DB_Request.Trang_thai == filter.value if filter else None,
    ]

    filter_conditions = filters.get(filter, default_condition)
    result = db.query(DB_Request).filter(and_(*filter_conditions)).all()

    db.close()
    return result
  
  @staticmethod
  async def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()

    status_text = STATUS.HOD_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.ACCT.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.Truong_BP_duyet: datetime.now()})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})

    db.commit()
    db.close()
    return result

  @staticmethod
  def get_notification():
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.HOD.value).all()

    return {
      "hod_accept": len(result)
    }