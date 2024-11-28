from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware
from config.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from contextvars import ContextVar

db_context: ContextVar = ContextVar("db_context")

engines = {
  "db1": create_engine(settings.DATABASE_URL1, pool_pre_ping=True),
  "db2": create_engine(settings.DATABASE_URL2, pool_pre_ping=True),
}

sessions = {key: sessionmaker(autocommit=False, autoflush=False, bind=engine) for key, engine in engines.items()}

def get_db() -> Session:
    db = db_context.get(None)
    if db is None:
        raise RuntimeError("Database session is not set")
    return db

class MultiDBMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        db_name = request.headers.get("X-DB-Name", "db2")
        if db_name not in sessions:
            return JSONResponse({"error": "Database không hợp lệ"}, status_code=400)
        
        db = sessions[db_name]()
        token = db_context.set(db) 
        try:
            response = await call_next(request)
        finally:
            db_context.reset(token)
            db.close()
        return response
    