from flask import render_template, flash, redirect, url_for
from application.forms import LoginForm, RegistrationForm
from application.models import User, Post
from application import app, db
from flask_login import logout_user, login_user, current_user

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Minever'}
    posts = Post.query.all()
    return render_template('index.html', user=user, posts=posts)

@app.route('/store')
def store():
    items = [
        {
            'title': "Python book",
            'price': 200
        },
        {
            'title': "Cook book",
            'price': 2
        },
        {
            'title': "iphone X",
            'price': 1000
        }

      ]
    return render_template('store.html', items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
     return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('login'))

    return render_template('login.html', title='Sign In', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if current_user.is_authenticated:
        return "You have been registered"
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data,email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))

    return render_template('signup.html', title='Register', form = form)


