from config.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

engines1 = create_engine(settings.DATABASE_URL1, pool_pre_ping=True)
engines2 = create_engine(settings.DATABASE_URL2, pool_pre_ping=True)

SessionLocalDB1 = sessionmaker(autocommit=False, autoflush=False, bind=engines1)
SessionLocalDB2 = sessionmaker(autocommit=False, autoflush=False, bind=engines2)

def get_db1() -> Session:
    db = SessionLocalDB1()
    try:
        return db
    except Exception as e:
        raise e
    finally:
        db.close()

def get_db2() -> Session:
    db = SessionLocalDB2()
    try:
        return db
    except Exception as e:
        raise e
    finally:
        db.close()