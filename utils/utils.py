from flask import request

def is_user_session_active():
    return request.cookies