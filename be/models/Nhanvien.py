from sqlalchemy import Column, Integer, String
from models.base import Base

class Nhanvien(Base):
    __tablename__ = "nhanvien"
    macongty = Column(String(10))
    masothe = Column(Integer)
    hoten = Column(String(50))
    phongban = Column(String(10))
    capbac = Column(String(10))
    phanquyen = Column(String(10))
    matkhau = Column(String(50))
    skylight = Column(String(50))
    id = Column(Integer, primary_key=True)
