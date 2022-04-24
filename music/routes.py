from flask import Blueprint, render_template, request

MUSIC_BLUEPRINT = Blueprint("music_routes", __name__, template_folder="templates")
BASE_ROUTE_PATH = "/songs"


@MUSIC_BLUEPRINT.route(BASE_ROUTE_PATH, methods=[ 'GET'])
def display_all_songs():
    if request.cookies.get("recommendo_user_active"):
        return render_template('Music.html')

@MUSIC_BLUEPRINT.route(BASE_ROUTE_PATH + '/<song_id>', methods=['POST', 'GET'])
def display_selected_song(song_id):
    if request.cookies.get("recommendo_user_active"):
        return render_template("Song_Solo.html")