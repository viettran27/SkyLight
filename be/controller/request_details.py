from fastapi import APIRouter
from repository.request_details import RequestDetailRepository
from schemas.RequestDetail import M_Request_Detail

router = APIRouter()

@router.get("/")
def get_requests(ma_pr: str):
  return RequestDetailRepository.get_requests(ma_pr)

@router.get("/search")
def get_requests_with_vt(ma_pr: str, ma_vat_tu: str):
  return RequestDetailRepository.get_requests_with_vt(ma_pr, ma_vat_tu)

@router.post("/")
def create_requests(data: M_Request_Detail):
  return RequestDetailRepository.create_request(data)

@router.put("/{id}")
def update_requests(id: int, data: M_Request_Detail):
  return RequestDetailRepository.update_request(id, data)

@router.delete("/{id}")
def delete_requests(id: int):
  return RequestDetailRepository.delete_request(id)