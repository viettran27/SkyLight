from services.request import RequestService
from schemas.Request import M_Request, M_Request_Approve
from enums.Request import STATUS_APPROVE, STATUS
from enums.Auth import POSTITON

class RequestRepository:
  @staticmethod
  def get_requests(phong_ban: str, chuc_vu: str):
    return RequestService.get_requests(phong_ban, chuc_vu)
  
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

    if status == STATUS_APPROVE.REJECTED:
      all_status = {
        POSTITON.HOD.value: STATUS.HOD_RJ.value,
        POSTITON.ACCT.value: STATUS.ACCT_RJ.value,
        POSTITON.CA.value: STATUS.CA_RJ.value,
        POSTITON.DIR.value: STATUS.DIR_RJ.value
      }
    else:
      all_status = {
        POSTITON.HOD.value: STATUS.ACCT.value,
        POSTITON.ACCT.value: STATUS.CA.value,
        POSTITON.CA.value: STATUS.DIR.value,
        POSTITON.DIR.value: STATUS.DONE.value
      }

    return RequestService.approve(all_status[auth], ma_pr)