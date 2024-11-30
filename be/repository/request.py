from services.request import RequestService
from schemas.Request import M_Request, M_Request_Approve
from enums.Request import STATUS_APPROVE, STATUS
from enums.Auth import POSITION
from positions import Hod, Req, Acct

class RequestRepository:
  positions = {
    POSITION.REQ: Req.REQ,
    POSITION.HOD: Hod.HOD,
    POSITION.ACCT: Acct.ACCT,
  }
  
  @staticmethod
  def get_requests(phong_ban: str, chuc_vu: POSITION):

    if chuc_vu == POSITION.REQ or chuc_vu == POSITION.HOD:
      all_requests = RequestRepository.positions[chuc_vu].get_requests(phong_ban)
    else:
      all_requests = RequestRepository.positions[chuc_vu].get_requests()
    return all_requests
  
  @staticmethod
  def get_requests_with_pr(ma_pr: str):
    return RequestService.get_requests_with_pr(ma_pr)

  @staticmethod
  def create_request(data: M_Request):
    return RequestService.create_request(data)
  
  @staticmethod
  def update_request(ma_pr: str, data: M_Request):
    return RequestService.update_request(ma_pr, data)
  
  @staticmethod
  def delete_request(ma_pr: str):
    return RequestService.delete_request(ma_pr)
  
  @staticmethod
  def approve(data: M_Request_Approve):
    status = data.Status
    auth = data.Auth
    ma_pr = data.Ma_PR

    return RequestRepository.positions[auth].approve(ma_pr, status)