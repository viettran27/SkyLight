from services.request import RequestService
from schemas.Request import M_Request

class RequestRepository:
  @staticmethod
  def get_requests():
    return RequestService.get_requests()

  @staticmethod
  def create_request(data: M_Request):
    return RequestService.create_request(data)
  
  @staticmethod
  def update_request(data: M_Request):
    return RequestService.update_request(data)
  
  @staticmethod
  def delete_request(ma_pr: str):
    return RequestService.delete_request(ma_pr)