from typing import Optional
from db.base import get_db2
from sqlalchemy import func, and_
from enums.Auth import POSTITON
from enums.Request import STATUS
from schemas.RequestDetail import M_Request_Detail
from models.RequestDetail import DB_Request_Detail
from services.request import RequestService
from datetime import datetime

class RequestDetailService:

  def __init__(self):
    pass

  @staticmethod
  def get_requests(ma_pr: str) -> list[DB_Request_Detail]:
    db = get_db2()
    all_details = db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr).all()
    db.close()
    return all_details
  
  @staticmethod
  def get_requests_with_vt(ma_pr:str, ma_vat_tu: str) -> list[DB_Request_Detail]:
    db = get_db2()
    all_details = db.query(DB_Request_Detail).filter(DB_Request_Detail.Ma_PR == ma_pr, func.lower(DB_Request_Detail.Ma_vat_tu).like(f"%{ma_vat_tu.lower()}%")).all()
    db.close()
    return all_details

  @staticmethod
  def create_request(data: M_Request_Detail) -> Optional[DB_Request_Detail]:
    db= get_db2()

    new_request_detail = DB_Request_Detail(
      Ma_PR=data.Ma_PR,
      Ma_vat_tu=data.Ma_vat_tu,
      Mo_ta=data.Mo_ta,
      Don_vi=data.Don_vi,
      So_luong=data.So_luong,
      Trang_thai=STATUS.HOD.value if POSTITON.REQ.value == data.Chuc_vu else STATUS.CA.value,
      Thoi_gian_yeu_cau=datetime.now(),
    )

    db.add(new_request_detail)
    db.commit()
    db.refresh(new_request_detail)
    db.close()
    return new_request_detail
  
  @staticmethod
  def update_request(id: int, data: M_Request_Detail) -> Optional[DB_Request_Detail]:
    db= get_db2()

    if data.Chuc_vu == POSTITON.REQ.value:
      result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).update({
        DB_Request_Detail.Ma_vat_tu: data.Ma_vat_tu,
        DB_Request_Detail.Mo_ta: data.Mo_ta,
        DB_Request_Detail.Don_vi: data.Don_vi,
        DB_Request_Detail.So_luong: data.So_luong,
      })
    else:
      data_exist = db.query(DB_Request_Detail).filter(
        and_(
          DB_Request_Detail.ID == id,
          DB_Request_Detail.Ma_vat_tu == data.Ma_vat_tu,
          DB_Request_Detail.Mo_ta ==  data.Mo_ta,
          DB_Request_Detail.Don_vi == data.Don_vi,
          DB_Request_Detail.So_luong == data.So_luong
        )
      ).first()
      
      if data_exist:
        result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).update({
          DB_Request_Detail.Ma_vat_tu: data.Ma_vat_tu,
          DB_Request_Detail.Mo_ta: data.Mo_ta,
          DB_Request_Detail.Don_vi: data.Don_vi,
          DB_Request_Detail.So_luong: data.So_luong,
          DB_Request_Detail.Don_gia: data.Don_gia,
          DB_Request_Detail.Thanh_tien: data.So_luong * (data.Don_gia or 0),
          DB_Request_Detail.Nha_cung_cap: data.Nha_cung_cap,
          DB_Request_Detail.Ngay_ve_du_kien: data.Ngay_ve_du_kien,  
        })
      else:
        print(getattr(data, "Don_gia", None))
        result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).update({
          DB_Request_Detail.Ma_vat_tu: data.Ma_vat_tu,
          DB_Request_Detail.Mo_ta: data.Mo_ta,
          DB_Request_Detail.Don_vi: data.Don_vi,
          DB_Request_Detail.So_luong: data.So_luong,
          DB_Request_Detail.Don_gia: getattr(data, "Don_gia", None),
          DB_Request_Detail.Thanh_tien: (data.So_luong * getattr(data, "Don_gia", None)) if getattr(data, "Don_gia", None) else None,
          DB_Request_Detail.Nha_cung_cap: getattr(data, "Nha_cung_cap", None),
          DB_Request_Detail.Ngay_ve_du_kien: getattr(data, "Ngay_ve_du_kien", None),
          DB_Request_Detail.Trang_thai: STATUS.ACCT_EDIT.value,
        })
        RequestService.update_status(data.Ma_PR, STATUS.ACCT_EDIT.value)
    db.commit()
    db.close()
    return result
  
  @staticmethod
  def delete_request(id: int) -> int:
    db = get_db2()
    result = db.query(DB_Request_Detail).filter(DB_Request_Detail.ID == id).delete()
    db.commit()
    db.close()
    return result