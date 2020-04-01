from flask import render_template, flash, redirect,url_for, request
from app import app
from app.forms import LoginForm, RegistrationForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User

@app.route('/')
@app.route('/index')
@login_required
def index():

    # user = {'username' : 'Tushar'}
    posts = [
        {
            'Author': {'username': 'Talha'},
            'Caption': 'Soft Computing has great Advantages'
        },
        {
            'Author': {'username': 'Rugved'},
            'Caption': 'Concurrency Control is nice topic!'
        }
    ]

    return render_template('index.html',title = "Home", posts = posts)

@app.route('/login',methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid Username or Password')
            return redirect(url_for('login'))

        # flash('Login requested for user {}, remember_me ={}'.format(
        #     form.username.data, form.remember_me.data))

        login_user(user, remember = form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index') 
        return redirect(url_for('index'))
    return render_template('login.html',title = 'Sign In',form = form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods = ['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username = username.data, email = email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)
