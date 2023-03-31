from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,login_user
from .forms import LoginForm , RegistrationForm
from app.models import User,db
from werkzeug.security import check_password_hash ,generate_password_hash

auth = Blueprint('auth' ,__name__ , url_prefix='/auth')



@auth.route('/create-account')
def create():
    return render_template('Login_SignUp/Login_Sign_Up.html'
    )

@auth.route('/register' , methods=["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(name = form.name.data , email = form.email.data , password = generate_password_hash(form.password.data))
        db.session.add(user)
        db.session.commit()
    return render_template('Login_SignUp/Sign_Up .html' , form = form)



@auth.route('/signin',methods=["GET","POST"])
def signin():
    sign_in = LoginForm()
    if sign_in.validate_on_submit():
        user = User.query.filter_by(email=sign_in.email.data).first()
        if user is not None and check_password_hash(sign_in.password.data , user.password):
            login_user(user)
            next = request.args.get('next')
            print('signin_sucessfull')
            return redirect(next or url_for('home.index'))
        flash ('Invalid email or password')
    return render_template('Login_SignUp/Login_In.html' , sign_in=sign_in)

@auth.route('/logout')
@login_required
def logout():
    return render_template('Login_SignUp/Login_Sign_Up.html')