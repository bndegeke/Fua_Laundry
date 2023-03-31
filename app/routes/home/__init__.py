from flask import Blueprint , render_template,redirect,url_for
from flask_login import login_required,current_user


home = Blueprint('home' , __name__ , url_prefix='/')


@home.route('/')
def index():
        return render_template('HOMEPAGE.html')
    