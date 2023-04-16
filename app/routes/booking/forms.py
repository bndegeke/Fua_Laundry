from flask_wtf import FlaskForm
from wtforms.validators import DataRequired , Email,EqualTo ,InputRequired
from wtforms.fields import StringField,PasswordField,SubmitField,DateField,SelectField
from  datetime import datetime


class BookingForm(FlaskForm):
    day = DateField('Day', validators=[InputRequired() ])
    laundry = SelectField('Payment Mode',choices=[('TYPE A','TYPE A'),('TYPE B' , 'TYPE B')] ,  validators=[DataRequired()])
    payment_mode = SelectField('Payment Mode',choices=[('MPESA','MPESA'),('CASH' , 'CASH')] ,  validators=[DataRequired()])
    location = StringField('Location' , validators=[DataRequired()])
    submit = SubmitField('Book')



