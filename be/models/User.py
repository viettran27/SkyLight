from pydantic import BaseModel

class User(BaseModel):
  macongty: str
  masothe: int
  matkhau: str

class UserInfo(BaseModel):
  macongty: str
  hoten: str
  phongban: str
  skylight: str
