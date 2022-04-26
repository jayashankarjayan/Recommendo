from xmlrpc.client import Boolean
from sqlalchemy import Column, String, Integer, Boolean
from utils.connection import Base

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)
    authenticated = Column(Boolean, default=False, nullable=False)
