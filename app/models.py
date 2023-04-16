from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from datetime import datetime


db = SQLAlchemy()


class User(UserMixin, db.Model):
    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(200) , nullable = False)
    email = db.Column(db.String(200) , nullable = False , unique=True)
    password = db.Column(db.String(200) , nullable = False )
    bookings = db.relationship("Booking" , backref="user")


class Booking(db.Model):
    id = db.Column(db.Integer , primary_key = True)
    date = db.Column(db.DateTime, nullable=False)
    type_laundry = db.Column(db.String(200) , nullable=False)
    payment = db.Column(db.String(200) , nullable = False) 
    location = db.Column(db.String(200) , nullable=False)
    completed = db.Column(db.Boolean , default = False)
    user_id = db.Column(db.Integer , db.ForeignKey('user.id'))
