import os
from flask import Flask
from routes import GENERIC_BLUEPRINT
from movies.routes import MOVIES_BLUEPRINT
from music.routes import MUSIC_BLUEPRINT
from shows.routes import SHOWS_BLUEPRINT
from books.routes import BOOKS_BLUEPRINT
from user.routes import USER_BLUEPRINT
from authentication.routes import AUTH_BLUEPRINT

APP = Flask(__name__)
APP.secret_key = os.urandom(32)

APP.register_blueprint(GENERIC_BLUEPRINT)
APP.register_blueprint(MOVIES_BLUEPRINT)
APP.register_blueprint(MUSIC_BLUEPRINT)
APP.register_blueprint(SHOWS_BLUEPRINT)
APP.register_blueprint(BOOKS_BLUEPRINT)
APP.register_blueprint(USER_BLUEPRINT)
APP.register_blueprint(AUTH_BLUEPRINT)

if __name__ == "__main__":
    APP.run(debug=True)

