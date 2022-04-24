from flask import Blueprint, render_template

GENERIC_BLUEPRINT = Blueprint("generic_routes", __name__, template_folder="templates")

@GENERIC_BLUEPRINT.route('/home', methods=['POST', 'GET'])
# @login_required
def home():
    return render_template('Home.html')

@GENERIC_BLUEPRINT.route("/about", methods=['POST', 'GET'])
def about():
    return render_template("About.html")

@GENERIC_BLUEPRINT.route("/explore", methods=['POST', 'GET'])
def explore():
    return render_template("Explore.html")

@GENERIC_BLUEPRINT.route('/recommendations', methods=['POST', 'GET'])
def rotd():
    return render_template("ROTD.html")
