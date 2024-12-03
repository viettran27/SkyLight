from models.Request import DB_Request
from models.RequestDetail import DB_Request_Detail
from db.base import get_db2
from sqlalchemy import text
from enums.Request import STATUS, STATUS_APPROVE, FILTER

class REQ:
  def __init__(self):
    pass

  @staticmethod
  def get_requests(phong_ban: str, filter: FILTER = None, search: str = None, page: int = 1, per_page: int = 10):
    db = get_db2()

    filters = {
      FILTER.ALL: [
        "Phong_ban = :phong_ban",
      ],
      FILTER.NOT_APPROVE: [
        "Phong_ban = :phong_ban",
        f"Trang_thai = N'{STATUS.ACCT_EDIT.value}'",
      ],
    }

    default_condition = [
      "Phong_ban = :phong_ban",
      f"Trang_thai = N'{filter.value}'",
    ]

    filter_conditions = filters.get(filter, default_condition)

    if search:
      filter_conditions.append("Ten_PR LIKE N'%{search}%'")

    filter_condition = " AND ".join(filter_conditions)

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
      "phong_ban": phong_ban,
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

    status_text = STATUS.REQ_RJ.value if STATUS_APPROVE.REJECTED == status else STATUS.REQ_ACPT.value

    result = db.query(DB_Request).filter(DB_Request.Ma_PR == ma_pr).update({DB_Request.Trang_thai: status_text})
    db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).update({DB_Request_Detail.Trang_thai: status_text})
    
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def get_notification():
    db = get_db2()
    result = db.query(DB_Request).filter(DB_Request.Trang_thai == STATUS.ACCT_EDIT.value).all()

    return {
      "req_edit": len(result)
    }