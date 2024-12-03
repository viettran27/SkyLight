from services.request import RequestService
from schemas.Request import M_Request, M_Request_Approve
from enums.Auth import POSITION
from enums.Request import FILTER
from positions import Hod, Req, Acct, Ca, Dir
from config.websocket import manager
import json

class RequestRepository:
  positions = {
    POSITION.REQ: Req.REQ,
    POSITION.HOD: Hod.HOD,
    POSITION.ACCT: Acct.ACCT,
    POSITION.CA: Ca.CA,
    POSITION.DIR: Dir.DIR
  }
  
  @staticmethod
  def get_requests(phong_ban: str, chuc_vu: POSITION, filter: FILTER = None, search: str = None, page: int = 1, per_page: int = 10):

    if chuc_vu == POSITION.REQ or chuc_vu == POSITION.HOD:
      all_requests = RequestRepository.positions[chuc_vu].get_requests(phong_ban, filter, search, page, per_page)
    else:
      all_requests = RequestRepository.positions[chuc_vu].get_requests(filter, search, page, per_page)
    return all_requests

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
  async def approve(data: M_Request_Approve):
    status = data.Status
    auth = data.Auth
    ma_pr = data.Ma_PR

    result = await RequestRepository.positions[auth].approve(ma_pr, status)
    notifications = RequestRepository.positions[auth].get_notification()
    await manager.broadcast(json.dumps(notifications))

    return result