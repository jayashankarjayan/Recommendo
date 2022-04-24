from sqlite3 import dbapi2
from colorama import reinit
from flask import Blueprint, request, render_template, redirect, session, url_for, flash
import form
from flask_login import login_user, login_required, current_user, logout_user
blueprint = Blueprint("all_routes", __name__, template_folder="templates")
from passlib.hash import sha256_crypt
from app import db, bcrypt, login_manager
from models import User
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base

my_conn = create_engine("mysql://root:@localhost/recommendo_login")
@blueprint.route('/Home', methods=['POST', 'GET'])
# @login_required
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
@login_manager.user_loader
def login():
    if request.method == "POST":
        # result = User.query.filter_by(username=request.form["Uname"]).first()
        # print(bcrypt.generate_password_hash(result.password))
        # if bcrypt.check_password_hash(result.password, request.form["Pass"]):
        #     result.authenticated = True
        #     db.session.add(result)
        #     db.session.commit()
        #     return render_template("Home.html")
        res = User.query.filter_by(username=request.form["Uname"]).first()
        print(sha256_crypt.encrypt("admin"))
        if sha256_crypt.verify(request.form["Pass"], sha256_crypt.encrypt("admin")):
            return render_template("Home.html")
        else:
            print("Res pwd:", res.password)
            print("SHA pwd:", sha256_crypt.encrypt("admin"))

    
    return render_template("login.html")


@blueprint.route("/Logout", methods=['GET'])
# @login_required
def logout():
    return render_template("login.html")

@blueprint.route("/NewUser", methods=['POST', 'GET'])
def newuser():
    if request.method == "POST":
        new_username = request.form["Uname"]
        new_pwd = request.form["Pass"]
        conf_pwd = request.form["ConfPass"]

        if new_pwd == conf_pwd:
            session = Session()
            Base = declarative_base()
            Base.metadata.create_all(db.engine)
            newuser = User(username=new_username, password=bcrypt.generate_password_hash(new_pwd))
            db.session.add(newuser)
            db.session.commit()
            return redirect(url_for("home"))

    return render_template("newuser.html")