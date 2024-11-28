from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.dialects.mssql import NVARCHAR

from models.base import Base

class DB_Request_Detail(Base):
    __tablename__ = "PR_chi_tiet"
    ID = Column(Integer, primary_key=True)
    Ma_PR = Column(String(10))
    Ma_vat_tu = Column(NVARCHAR(100))
    Mo_ta = Column(NVARCHAR(200))
    Don_vi = Column(NVARCHAR(20))
    So_luong = Column(Integer)
    Don_gia = Column(Integer)
    Thanh_tien = Column(Integer)
    Nha_cung_cap = Column(NVARCHAR(100))
    Trang_thai = Column(NVARCHAR(50))
    Ngay_ve_du_kien = Column(Date)
    Thoi_diem_dat_hang = Column(DateTime)
    Thoi_diem_ve_kho = Column(DateTime)
    Thoi_gian_yeu_cau = Column(DateTime)
    Ghi_chu = Column(NVARCHAR(500))
