from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash , check_password_hash
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(200) , nullable = False)
    email = db.Column(db.String(200) , nullable = False , unique=True)
    password = db.Column(db.String(200) , nullable = False )



@login_manager.user_loader
def load_user(user_id):
    return User.get_id(user_id)