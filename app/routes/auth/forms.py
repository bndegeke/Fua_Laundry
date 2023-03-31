from flask_wtf import FlaskForm
from wtforms.validators import DataRequired , Email,EqualTo
from wtforms.fields import StringField,PasswordField,SubmitField



class RegistrationForm(FlaskForm):
    name = StringField('Name' , validators=[DataRequired()])
    email = StringField('Email' , validators=[DataRequired() , Email()])
    password = StringField('Email' , validators=[DataRequired()])
    submit = SubmitField('SIGN UP')



class LoginForm(FlaskForm):
    email = StringField('Email' , validators=[DataRequired() , Email()])
    password = StringField('Email' , validators=[DataRequired()])
    submit = SubmitField('SIGN IN')