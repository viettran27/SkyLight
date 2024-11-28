from fastapi import APIRouter, Request
from repository.request import RequestRepository
from config.config import settings
from schemas.Request import M_Request

router = APIRouter()

@router.get("/")
def get_requests():
  return RequestRepository.get_requests()

@router.post("/")
def create_requests(data: M_Request):
  return RequestRepository.create_request(data)

@router.patch("/update")
def update_requests(data: M_Request):
  return RequestRepository.update_request(data)

@router.delete("/")
def delete_requests(ma_pr: str):
  return RequestRepository.delete_request(ma_pr)