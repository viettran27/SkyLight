from fastapi import APIRouter
from repository.request import RequestRepository
from schemas.Request import M_Request, M_Request_Approve

router = APIRouter()

@router.get("/")
def get_requests(phong_ban:str, chuc_vu:str):
  return RequestRepository.get_requests(phong_ban, chuc_vu)

@router.get("/search")
def get_requests_with_pr(ma_pr: str):
  return RequestRepository.get_requests_with_pr(ma_pr)

@router.post("/")
def create_requests(data: M_Request):
  return RequestRepository.create_request(data)

@router.put("/{ma_pr}")
def update_requests(ma_pr: str, data: M_Request):
  return RequestRepository.update_request(ma_pr, data)

@router.delete("/{ma_pr}")
def delete_requests(ma_pr: str):
  return RequestRepository.delete_request(ma_pr)

@router.post("/approve")
def approve(data: M_Request_Approve):
  return RequestRepository.approve(data)


