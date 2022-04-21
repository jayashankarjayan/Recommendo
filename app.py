from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import null

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:''@localhost/recommendo_login'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    username = db.Column(db.String(50), primary_key = True)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<User %r>' %self.username


@app.route('/Home', methods=['POST', 'GET'])
def home():
    return render_template('Home.html')

@app.route('/Books', methods=['POST', 'GET']) 

def books():
    return render_template('Books.html')

@app.route('/Movies', methods=['POST', 'GET'])

def movies():
    return render_template('Movies.html')

@app.route("/TV_Shows", methods=['POST', 'GET'])

def tvshows():
    return render_template('TV_Shows.html')

@app.route('/Music', methods=['POST', 'GET'])

def music():
    return render_template('Music.html')


@app.route("/About", methods=['POST', 'GET'])

def about():
    return render_template("About.html")

@app.route("/Explore", methods=['POST', 'GET'])

def explore():
    return render_template("Explore.html")

@app.route('/ROTD', methods=['POST', 'GET'])

def rotd():
    return render_template("ROTD.html")


@app.route('/Book_Solo', methods=['POST', 'GET'])

def booksolo():
    return render_template("Book_Solo.html")

@app.route('/Movie_Solo', methods=['POST', 'GET'])

def moviesolo():
    return render_template("Movie_Solo.html")

@app.route('/Song_Solo', methods=['POST', 'GET'])

def songsolo():
    return render_template("Song_Solo.html")

@app.route('/TV_Show_Solo', methods=['POST', 'GET'])

def tvshowsolo():
    return render_template("TV_Show_Solo.html")



@app.route("/Login", methods=['POST', 'GET'])

def login():
    if request.method == 'POST':
        username = request.form['Uname']
        password = request.form['Pass']
        all_users = User.query.filter_by(username="admin").all()
        print(all_users.username)
        return redirect(url_for("home"), all_users=all_users)
    else:
        return render_template("login.html")




if __name__ == "__main__":
    app.run(debug=True)