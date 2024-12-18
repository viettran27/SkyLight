from typing import Optional
from db.base import get_db1
from schemas.User import User
from models.Nhanvien import Nhanvien

class AuthService:
    def __init__(self):
        pass

    @staticmethod
    def authenticate(i_user: User) -> Optional[User]:
        db = get_db1()
        user = db.query(Nhanvien).filter_by(macongty=i_user.macongty, masothe=i_user.masothe).first()
        if not user:
            return None
        if user.matkhau != i_user.matkhau:
            return None
        db.close()
        return user
    
    @staticmethod
    def getUser(masothe: int, macongty: str) -> User:
        db = get_db1()
        user = db.query(Nhanvien).filter_by(masothe=masothe, macongty=macongty).first()
        db.close()
        return user