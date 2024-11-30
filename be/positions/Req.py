from models.Request import DB_Request
from db.base import get_db2

class REQ:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(phong_ban: str):
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Phong_ban == phong_ban).all()

    db.close()
    return result