from passlib.hash import sha256_crypt
from app import User, db

from sqlalchemy.orm import Session, sessionmaker

session = Session(bind=db.engine)
passw = 'admin'
user = User(username="admin", password=sha256_crypt.encrypt("admin"))
session.add(user)
session.commit()
