from models.Request import DB_Request
from db.base import get_db2
from sqlalchemy import and_
from enums.Request import STATUS

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