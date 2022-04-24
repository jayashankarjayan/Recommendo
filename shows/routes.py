from flask import Blueprint, render_template, request

SHOWS_BLUEPRINT = Blueprint("show_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/shows"

@SHOWS_BLUEPRINT.route(BASE_ROUTE_PATH, methods=['GET'])
def display_all_shows():
    if request.cookies.get("recommendo_user_active"):
        return render_template('TV_Shows.html')


@SHOWS_BLUEPRINT.route(BASE_ROUTE_PATH + '/<show_id>', methods=['GET'])
def display_selected_show(show_id):
    if request.cookies.get("recommendo_user_active"):
        return render_template("TV_Show_Solo.html")
