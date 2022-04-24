from flask import Blueprint, render_template, \
                  request, make_response

from user.user import UserOperations

AUTH_BLUEPRINT = Blueprint("authentication_routes", __name__, template_folder="templates")
LOGIN_PAGE = "login.html"

@AUTH_BLUEPRINT.route("/login", methods=['GET'])
def display_login_page():
    return render_template(LOGIN_PAGE)

@AUTH_BLUEPRINT.route("/login", methods=['POST'])
def validate_user():
    is_valid_user = UserOperations().user_exists(request.form)
    if is_valid_user:
        response = make_response(render_template("Home.html"))
        response.set_cookie("recommendo_user_active", "True")
        return response
    else:
        message = "Invalid username or password"
        return render_template(LOGIN_PAGE, message=message, error=True)

@AUTH_BLUEPRINT.route("/logout", methods=['GET'])
def logout():
    return render_template(LOGIN_PAGE)