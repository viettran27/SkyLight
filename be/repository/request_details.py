from services.request_details import RequestDetailService
from schemas.RequestDetail import M_Request_Req, M_Request_Req_Update

class RequestDetailRepository:
  @staticmethod
  def get_requests(ma_pr: str):
    return RequestDetailService.get_requests(ma_pr)

  @staticmethod
  def get_requests_with_vt(ma_pr: str, ma_vat_tu: str):
    return RequestDetailService.get_requests_with_vt(ma_pr, ma_vat_tu)

  @staticmethod
  def create_request(data: M_Request_Req):
    return RequestDetailService.create_request(data)
  
  @staticmethod
  def update_request(id: int, data: M_Request_Req_Update):
    return RequestDetailService.update_request(id, data)
  
  @staticmethod
  def delete_request(id: int):
    return RequestDetailService.delete_request(id)