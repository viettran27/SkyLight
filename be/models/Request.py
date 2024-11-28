from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.dialects.mssql import NVARCHAR

from models.base import Base

class DB_Request(Base):
    __tablename__ = "PR"
    Ma_PR = Column(String(20), primary_key=True)
    Phong_ban = Column(String(10))
    Ten_PR = Column(NVARCHAR(100))
    Muc_dich = Column(NVARCHAR(200))
    Tong_so_tien = Column(Integer)
    Ngay_can = Column(Date)
    Nguoi_yeu_cau = Column(NVARCHAR(50))
    Thoi_gian_yeu_cau = Column(DateTime)
    Truong_BP_duyet = Column(DateTime)
    Ke_toan_phe_duyet = Column(DateTime)
    BLD_phe_duyet = Column(DateTime)
    Thoi_diem_dat_hang = Column(DateTime)
    Thoi_diem_ve_kho = Column(DateTime)
    Trang_thai = Column(NVARCHAR(50))
    Ghi_chu = Column(NVARCHAR(500))
