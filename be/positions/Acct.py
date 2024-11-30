from models.Request import DB_Request
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS

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