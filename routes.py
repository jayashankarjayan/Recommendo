from flask import Blueprint, request, render_template, redirect, url_for


blueprint = Blueprint("all_routes", __name__, template_folder="templates")

@blueprint.route('/Home', methods=['POST', 'GET'])
def home():
    return render_template('Home.html')

@blueprint.route('/Books', methods=['POST', 'GET']) 
def books():
    return render_template('Books.html')

@blueprint.route('/Movies', methods=['POST', 'GET'])
def movies():
    return render_template('Movies.html')

@blueprint.route("/TV_Shows", methods=['POST', 'GET'])
def tvshows():
    return render_template('TV_Shows.html')

@blueprint.route('/Music', methods=['POST', 'GET'])
def music():
    return render_template('Music.html')

@blueprint.route("/About", methods=['POST', 'GET'])
def about():
    return render_template("About.html")

@blueprint.route("/Explore", methods=['POST', 'GET'])
def explore():
    return render_template("Explore.html")

@blueprint.route('/ROTD', methods=['POST', 'GET'])
def rotd():
    return render_template("ROTD.html")

@blueprint.route('/Book_Solo', methods=['POST', 'GET'])
def booksolo():
    return render_template("Book_Solo.html")

@blueprint.route('/Movie_Solo', methods=['POST', 'GET'])
def moviesolo():
    return render_template("Movie_Solo.html")

@blueprint.route('/Song_Solo', methods=['POST', 'GET'])
def songsolo():
    return render_template("Song_Solo.html")

@blueprint.route('/TV_Show_Solo', methods=['POST', 'GET'])
def tvshowsolo():
    return render_template("TV_Show_Solo.html")

@blueprint.route("/Login", methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['Uname']
        password = request.form['Pass']
        all_users = User.query.filter_by(username="admin").all()
        print(all_users.username)
        return redirect(url_for("home"), all_users=all_users)
    else:
        return render_template("login.html")
