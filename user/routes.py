from flask import Blueprint, render_template, \
                  request, redirect, url_for
from user.user import UserOperations
from utils.custom_exceptions import PasswordMismatch

USER_BLUEPRINT = Blueprint("user_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/users"

@USER_BLUEPRINT.route(BASE_ROUTE_PATH + "/new", methods=['GET'])
def display_new_user_page():
    return render_template("newuser.html")

@USER_BLUEPRINT.route(BASE_ROUTE_PATH + "/new", methods=['POST'])
def create_new_user():
    try:
        registration_status = UserOperations().register_new_user(request.form)
    except PasswordMismatch as why:
        message = str(why)
        registration_status = False

    if registration_status:
        return redirect(url_for("home"))
    else:
        # TODO: Redirect to the new user page indicating failure
        return render_template("newuser.html", message=message)