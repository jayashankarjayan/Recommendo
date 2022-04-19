from flask import Flask, request, render_template, redirect, url_for
import pandas as pd

app = Flask(__name__)

ratings = pd.read_csv("ml-latest-small/ratings.csv")


@app.route('/Home', methods=['POST', 'GET'])

def home():
    return render_template('Home.html')


@app.route('/Books', methods=['POST', 'GET']) 

def books():
    return render_template('Books.html')

@app.route('/Movies', methods=['POST', 'GET'])

def movies():
    return render_template('Movies.html', ratings=ratings.to_dict())

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
    error = None
    if request.method == 'POST':
        if request.form['Uname'] != 'admin' or request.form['Pass'] != 'admin':
            error = 'Invalid Credentials. Please Try Again'
        
        else:
            return redirect(url_for('home'))
    
    return render_template('login.html', error=error)




if __name__ == "__main__":
    app.run(debug=True)