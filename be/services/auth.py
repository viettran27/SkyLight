from typing import Optional
from fastapi_sqlalchemy import db
from models.User import User
from schemas.nhanvien import Nhanvien

class AuthService:
    def __init__(self):
        pass

    @staticmethod
    def authenticate(i_user: User) -> Optional[User]:
        user = db.session.query(Nhanvien).filter_by(macongty=i_user.macongty, masothe=i_user.masothe).first()
        if not user:
            return None
        if user.matkhau != i_user.matkhau:
            return None
        return user
    
    @staticmethod
    def getUser(masothe: int, macongty: str) -> User:
        return db.session.query(Nhanvien).filter_by(masothe=masothe, macongty=macongty).first()