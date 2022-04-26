import hashlib
from models.entity import User
from utils.connection import session
import pandas as pd

passw = hashlib.md5("admin".encode("UTF-8")).hexdigest()
user = User(username="admin", password=passw)
session.add(user)
session.commit()

users_data = pd.read_csv("user_creds.csv")
for ind in users_data.index:
    if list(users_data["Username"]).count(users_data["Username"][ind]) == 1:
        passw = hashlib.md5(users_data["Password"][ind].encode("UTF-8")).hexdigest()
        user = User(username=users_data["Username"][ind], password=passw, authenticated=False)
        session.add(user)
        session.commit()

