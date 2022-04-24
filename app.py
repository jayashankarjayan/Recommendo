from flask import Flask
from flask_login import LoginManager, login_required

from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from sqlalchemy import orm 

app = Flask(__name__)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost/recommendo_login"
app.secret_key = "My Secret Key"

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

from routes import blueprint
app.register_blueprint(blueprint)

from models import User
@login_manager.user_loader
def load_user(user_id):
    try:
        return User.query.get(user_id)
    except:
        return None

@login_required
def loginreq():
    pass


        

if __name__ == "__main__":
    app.run(debug=True)

