from flask import Blueprint, render_template, request

GENERIC_BLUEPRINT = Blueprint("generic_routes", __name__, template_folder="templates")

@GENERIC_BLUEPRINT.route('/Home', methods=['GET'])
def home():
    if request.cookies.get("recommendo_user_active"):
        return render_template('Home.html')

@GENERIC_BLUEPRINT.route("/about", methods=['GET'])
def about():
    if request.cookies.get("recommendo_user_active"):
        return render_template("About.html")

@GENERIC_BLUEPRINT.route("/Explore", methods=['GET'])
def explore():
    if request.cookies.get("recommendo_user_active"):
        return render_template("Explore.html")

@GENERIC_BLUEPRINT.route('/ROTD', methods=['GET'])
def rotd():
    if request.cookies.get("recommendo_user_active"):
        return render_template("ROTD.html")
