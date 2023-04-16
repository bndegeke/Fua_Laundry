from flask import Blueprint,render_template,request,redirect,url_for,flash
from flask_login import login_required,login_user,current_user
from .forms import LoginForm , RegistrationForm
from app.models import User,db
from werkzeug.security import check_password_hash ,generate_password_hash

auth = Blueprint('auth' ,__name__ , url_prefix='/auth')



@auth.route('/register' , methods=["GET","POST"])
def register():
    sign_up = RegistrationForm()
    if sign_up.validate_on_submit():
        user = User.query.filter_by(email = sign_up.email.data).first()
        if  user:
            flash ('Email address already exists')
        else:
            new_user = User(
                name = sign_up.name.data , 
                email = sign_up.email.data , 
                password = generate_password_hash(sign_up.password.data)
                )
            db.session.add(new_user)
            db.session.commit()
            return redirect (url_for('auth.signin'))
    return render_template('Login_SignUp/SignUp.html' , sign_up = sign_up)



@auth.route('/signin',methods=["GET","POST"])
def signin():
    sign_in = LoginForm()
    if sign_in.validate_on_submit():
        user = User.query.filter_by(email=sign_in.email.data).first()
        if not user  and  not check_password_hash(sign_in.password.data , user.password):
            flash ('Invalid email or password')
        else:
            login_user(user,remember=True)
            next = request.args.get('next')
            print('signin_sucessfull')
            return redirect(next or url_for('home.index'))

    return render_template('Login_SignUp/Login_In.html' , sign_in=sign_in)

@auth.route('/logout')
@login_required
def logout():
    return render_template('Login_SignUp/Login_Sign_Up.html')



@auth.route('/profile')
@login_required
def profile():
    return render_template('profile.html' , name = current_user.name)