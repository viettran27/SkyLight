from fastapi import APIRouter, Request
from repository.request_details import RequestDetailRepository
from config.config import settings
from schemas.RequestDetail import M_Request_Not_Req, M_Request_Req

router = APIRouter()

@router.get("/")
def get_requests(ma_pr: str):
  return RequestDetailRepository.get_requests(ma_pr)

@router.post("/")
def create_requests(data: M_Request_Req | M_Request_Not_Req):
  return RequestDetailRepository.create_request(data)

@router.patch("/update")
def update_requests(id: int, data: M_Request_Req | M_Request_Not_Req):
  return RequestDetailRepository.update_request(id, data)

@router.delete("/")
def delete_requests(id: int):
  return RequestDetailRepository.delete_request(id)