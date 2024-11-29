from services.request import RequestService
from schemas.Request import M_Request, M_Request_Approve, Status_Approve

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

    if status == Status_Approve.REJECTED:
      all_status = {
        "hod": "Trưởng bộ phận từ chối",
        "acct": "Kế toán từ chối",
        "ca": "Trưởng kế toán từ chối",
        "dir": "Lãnh đạo từ chối"
      }
    else:
      all_status = {
        "hod": "Đang đợi kế toán duyệt",
        "acct": "Đang đợi kế toán trưởng duyệt",
        "ca": "Đang đợi duyệt cuối cùng",
        "dir": "Đã duyệt"
      }

    return RequestService.approve(all_status[auth], ma_pr)