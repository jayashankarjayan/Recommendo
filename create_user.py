import hashlib
from models.entity import User
from utils.connection import session

passw = hashlib.md5("admin".encode("UTF-8")).hexdigest()
user = User(username="admin", password=passw)
session.add(user)
session.commit()
