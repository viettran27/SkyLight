from fastapi import APIRouter
from controller import auth, requests, request_details

router = APIRouter()

router.include_router(auth.router, tags=["Auth"], prefix="/v1/auth")
router.include_router(requests.router, tags=["Requests"], prefix="/v1/requests")
router.include_router(request_details.router, tags=["Request Details"], prefix="/v1/request_details")


