from fastapi import APIRouter, Request
from repository.auth import AuthRepository
from models.User import User
from models.Auth import Token
from config.config import settings

router = APIRouter()

@router.post("/login")
def login(user: User):
    return AuthRepository.login(user)

@router.post("/refresh")
def refresh(token: Token):
    return AuthRepository.refresh(token)

@router.get("/me")
def getMe(request: Request):
    auth_header = request.headers.get('Authorization')
    if not auth_header and not auth_header.split(' ')[1]:
        return None
    
    access_token = auth_header.split(' ')[1]
    return AuthRepository.getMe(access_token)   

