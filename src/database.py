from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import Column, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

from config import SQL_URL

Base = declarative_base()


class UserToQQ(Base):
    __tablename__ = "user_to_qq"
    
    id = Column(Integer, primary_key=True, index=True)
    wx_id = Column(VARCHAR(126), unique=True, server_default='')
    qq = Column(VARCHAR(126), unique=True, server_default='')
    
    class Config:
        orm_mode = True


SQLALCHEMY_DATABASE_URL = SQL_URL

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
