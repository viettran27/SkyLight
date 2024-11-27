from fastapi import APIRouter
from controller import auth

router = APIRouter()

router.include_router(auth.router, tags=["Auth"], prefix="/auth")


