from services.request_details import RequestDetailService
from schemas.RequestDetail import M_Request_Req, M_Request_Not_Req

class RequestDetailRepository:
  @staticmethod
  def get_requests(ma_pr: str):
    return RequestDetailService.get_requests(ma_pr)

  @staticmethod
  def create_request(data: M_Request_Req | M_Request_Not_Req):
    return RequestDetailService.create_request(data)
  
  @staticmethod
  def update_request(id: int, data: M_Request_Req | M_Request_Not_Req):
    return RequestDetailService.update_request(id, data)
  
  @staticmethod
  def delete_request(id: int):
    return RequestDetailService.delete_request(id)