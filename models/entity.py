import os
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import Column, String
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

load_dotenv()
DB_NAME = os.environ.get("DB_NAME") 
DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_HOST = os.environ.get("DB_HOST")
CONN = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

Base = declarative_base()
engine = create_engine(CONN, future=True)
session = Session(engine)


class User(Base):
    __tablename__ = 'user'

    username = Column(String(50), primary_key = True)
    password = Column(String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' %self.username