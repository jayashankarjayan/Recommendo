from app import db
from app import login_manager
from sqlalchemy.orm import Session, declarative_base

class User(db.Model):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}
    username = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(50), nullable=False)
    authenticated = db.Column(db.Boolean, default=False)

    def is_active(self):
        return True
    
    def get_id(self):
        return self.username

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False



