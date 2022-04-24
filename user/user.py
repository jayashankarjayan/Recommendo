from base64 import encode
import hashlib
from utils.connection import session
from utils.custom_exceptions import PasswordMismatch
from models.entity import User

class UserOperations:

    def register_new_user(self, data):
        status = False
        username = data["Uname"].strip()
        password = hashlib.md5(data["Pass"].strip().encode("UTF-8")).hexdigest()
        password_confirmation = hashlib.md5(data["ConfPass"].strip().encode("UTF-8")).hexdigest()
        if password != password_confirmation:
            raise PasswordMismatch("Two passwords do not match")

        newuser = User(username=username, password=password)
        session.add(newuser)
        session.commit()
        status = True
        return status
    

    def user_exists(self, data):
        status = False
        username = data.get("Uname").strip()
        password = hashlib.md5(data.get("Pass").strip().encode("UTF-8")).hexdigest()

        record_count = session.query(User.username)\
                        .filter(User.username == username)\
                        .filter(User.password == password)\
                        .count()

        if record_count == 1:
            status = True

        return status