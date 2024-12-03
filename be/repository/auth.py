from fastapi import HTTPException
from fastapi.responses import JSONResponse
from services.auth import AuthService
from schemas.User import User, UserInfo
from schemas.Auth import Token
from config.config import settings
import datetime
import jwt

class AuthRepository:

    @staticmethod
    def create_jwt_token(data: dict, expires_delta: datetime.timedelta):
        payload = data.copy()
        payload["exp"] = datetime.datetime.utcnow() + expires_delta
        return jwt.encode(payload, settings.SECRET_KEY, algorithm=settings.SECURITY_ALGORITHM)
    
    @staticmethod
    def login(user: User):
        user = AuthService.authenticate(user)
        if not user:
            return HTTPException(status_code=404, detail="Không tìm thấy nhân viên")

        access_token = AuthRepository.create_jwt_token({"mst": user.masothe, "fac": user.macongty, "position": user.skylight, "type": "access"}, expires_delta=datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))
        refresh_token = AuthRepository.create_jwt_token({"mst": user.masothe,"fac": user.macongty, "position": user.skylight, "type": "refresh"}, expires_delta=datetime.timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS))
        user_info = UserInfo(
            macongty=user.macongty,
            hoten=user.hoten,
            phongban=user.phongban,
            skylight=user.skylight
        )
        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "user": user_info.dict() 
        }

    @staticmethod
    def refresh(token: Token):  
        try:
            decoded_refresh_token = jwt.decode(token.refresh_token, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
            if decoded_refresh_token.get("type") != "refresh":
                raise HTTPException(status_code=400, detail="Invalid token type")
            masothe = decoded_refresh_token.get("mst")
            macongty = decoded_refresh_token.get("fac")
            macongty = decoded_refresh_token.get("fac")
            position = decoded_refresh_token.get("position")
            access_token = AuthRepository.create_jwt_token({"mst": masothe, "fac": macongty, "position": position,"type": "access"}, expires_delta=datetime.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES))

            return JSONResponse(content={"access_token": access_token})

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Refresh token hết hạn")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Refresh token không đúng")

    @staticmethod
    def getMe(access_token: str):
        try:
            decoded_access_token = jwt.decode(access_token, settings.SECRET_KEY, algorithms=[settings.SECURITY_ALGORITHM])
            if decoded_access_token.get("type") != "access":
                raise HTTPException(status_code=400, detail="Invalid token type")
            masothe = decoded_access_token.get("mst")
            macongty = decoded_access_token.get("fac")
            
            user = AuthService.getUser(masothe, macongty)
            user = UserInfo(
                macongty=macongty,
                hoten=user.hoten,
                phongban=user.phongban,
                skylight=user.skylight
            )

            return user
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="access_token hết hạn")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="access_token không đúng")