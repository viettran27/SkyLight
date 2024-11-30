from services.request_details import RequestDetailService
from schemas.RequestDetail import M_Request_Detail

class RequestDetailRepository:
  @staticmethod
  def get_details(ma_pr: str):
    return RequestDetailService.get_details(ma_pr)

  @staticmethod
  def get_details_with_vt(ma_pr: str, ma_vat_tu: str):
    return RequestDetailService.get_details_with_vt(ma_pr, ma_vat_tu)

  @staticmethod
  def create_detail(data: M_Request_Detail):
    return RequestDetailService.create_detail(data)
  
  @staticmethod
  def update_detail(id: int, data: M_Request_Detail):
    return RequestDetailService.update_detail(id, data)
  
  @staticmethod
  def delete_detail(id: int):
    return RequestDetailService.delete_detail(id)