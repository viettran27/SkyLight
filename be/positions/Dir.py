from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import text
from enums.Request import STATUS, STATUS_APPROVE, FILTER
from datetime import datetime

class DIR:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(filter: FILTER = None, search: str = None, page: int = 1, per_page: int = 10):
    db = get_db2()
  
    filters = {
      FILTER.ALL: [
        f"Trang_thai = N'{STATUS.DIR.value}'",
        f"Trang_thai = N'{STATUS.DIR_ACPT.value}'",
        f"Trang_thai = N'{STATUS.DIR_RJ.value}'",
        f"Trang_thai = N'{STATUS.ACCT_ORDERED.value}'"
      ],
      FILTER.APPROVED: [
        f"Trang_thai = N'{STATUS.DIR_ACPT.value}'",
        f"Trang_thai = N'{STATUS.ACCT_ORDERED.value}'"
      ],
      FILTER.NOT_APPROVE: [
        f"Trang_thai = N'{STATUS.DIR.value}'"
      ],
    }

    default_condition = [f"Trang_thai = N'{filter.value}'"]
    filter_conditions = filters.get(filter, default_condition)

    filter_condition = " OR ".join(filter_conditions)

    if search:
      filter_condition = f"({filter_condition}) AND Ten_PR LIKE N'%{search}%'"

    start_row = (page - 1) * per_page + 1
    end_row = page * per_page

    query = f"""
      SELECT * FROM (
          SELECT 
              ROW_NUMBER() OVER (ORDER BY Thoi_gian_yeu_cau DESC) AS RowNum, * 
          FROM PR 
          WHERE {filter_condition}
      ) AS RowConstrainedResult
      WHERE RowNum BETWEEN :start_row AND :end_row
    """

    params = {
      "start_row": start_row,
      "end_row": end_row,
    }

    result = db.execute(text(query), params).fetchall()

    total_query = f"""
      SELECT COUNT(*) FROM PR 
      WHERE {filter_condition}
    """
    total_records = db.execute(text(total_query), params).scalar()

    db.close()

    return {
      "data": [dict(row._mapping) for row in result],
      "total": total_records,
      "current_page": page,
      "per_page": per_page
    }
  
  @staticmethod
  async def approve(ma_pr:str, status: STATUS_APPROVE):
    db = get_db2()

    status_text = STATUS.DIR_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.DIR_ACPT.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text, DB_Request.BLD_phe_duyet: datetime.now()})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})
    
    db.commit()
    db.close()
    return result

  @staticmethod
  def get_notification():
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.DIR.value).all()

    return {
      "dir_accept": len(result)
    }