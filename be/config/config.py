import os
from dotenv import load_dotenv
from sqlalchemy.engine import URL

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
load_dotenv(os.path.join(BASE_DIR, '.env'))

class Settings():
    SECRET_KEY = os.getenv('SECRET_KEY', '')
    API_PREFIX = ''
    BACKEND_CORS_ORIGINS = ['http://localhost:5173']
    DATABASE_URL1 = URL.create(
        "mssql+pyodbc",
        username=os.getenv("USERNAME_DB"),
        password=os.getenv("PASSWORD_DB"),
        host=os.getenv("HOST"),
        port=1433,
        database=os.getenv("DATABASE1"),
        query={
           "driver": "ODBC Driver 17 for SQL Server",
           "TrustServerCertificate": "yes" 
        }
    )
    DATABASE_URL2 = URL.create(
        "mssql+pyodbc",
        username=os.getenv("USERNAME_DB"),
        password=os.getenv("PASSWORD_DB"),
        host=os.getenv("HOST"),
        port=1433,
        database=os.getenv("DATABASE2"),
        query={
           "driver": "ODBC Driver 17 for SQL Server",
           "TrustServerCertificate": "yes" 
        }
    )
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 1
    REFRESH_TOKEN_EXPIRE_DAYS:int = 1
    SECURITY_ALGORITHM = 'HS256'

settings = Settings()