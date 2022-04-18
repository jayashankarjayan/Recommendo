from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

ratings = pd.read_csv("ml-latest-small/ratings.csv")


@app.route('/Home.html', methods=['POST', 'GET'])

def home():
    return render_template('Home.html')


@app.route('/Books.html', methods=['POST', 'GET']) 

def books():
    return render_template('Books.html')

@app.route('/Movies.html', methods=['POST', 'GET'])

def movies():
    return render_template('Movies.html', ratings=ratings.to_dict())

@app.route("/TV_Shows.html", methods=['POST', 'GET'])

def tvshows():
    return render_template('TV_Shows.html')

@app.route('/Music.html', methods=['POST', 'GET'])

def music():
    return render_template('Music.html')


@app.route("/About.html", methods=['POST', 'GET'])

def about():
    return render_template("About.html")

@app.route("/Explore.html", methods=['POST', 'GET'])

def explore():
    return render_template("Explore.html")

@app.route('/ROTD.html', methods=['POST', 'GET'])

def rotd():
    return render_template("ROTD.html")


@app.route('/Book_Solo.html', methods=['POST', 'GET'])

def booksolo():
    return render_template("Book_Solo.html")

@app.route('/Movie_Solo.html', methods=['POST', 'GET'])

def moviesolo():
    return render_template("Movie_Solo.html")

@app.route('/Song_Solo.html', methods=['POST', 'GET'])

def songsolo():
    return render_template("Song_Solo.html")

@app.route('/TV_Show_Solo.html', methods=['POST', 'GET'])

def tvshowsolo():
    return render_template("TV_Show_Solo.html")

if __name__ == "__main__":
    app.run(debug=True)