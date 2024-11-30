from fastapi import APIRouter
from repository.request_details import RequestDetailRepository
from schemas.RequestDetail import M_Request_Detail

router = APIRouter()

@router.get("/")
def get_details(ma_pr: str):
  return RequestDetailRepository.get_details(ma_pr)

@router.get("/search")
def get_details_with_vt(ma_pr: str, ma_vat_tu: str):
  return RequestDetailRepository.get_details_with_vt(ma_pr, ma_vat_tu)

@router.post("/")
def create_detail(data: M_Request_Detail):
  return RequestDetailRepository.create_detail(data)

@router.put("/{id}")
def update_detail(id: int, data: M_Request_Detail):
  return RequestDetailRepository.update_detail(id, data)

@router.delete("/{id}")
def delete_detail(id: int):
  return RequestDetailRepository.delete_detail(id)