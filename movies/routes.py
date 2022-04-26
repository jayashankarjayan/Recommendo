from flask import Blueprint, render_template, request

MOVIES_BLUEPRINT = Blueprint("movie_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/Movies"

@MOVIES_BLUEPRINT.route(BASE_ROUTE_PATH, methods=['GET'])
def display_all_movies():
    if request.cookies.get("recommendo_user_active"):
        return render_template('Movies.html')

@MOVIES_BLUEPRINT.route("/Movie_Solo", methods=['GET'])
def display_selected_movie():
    if request.cookies.get("recommendo_user_active"):
        return render_template("Movie_Solo.html")
