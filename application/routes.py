from flask import render_template, flash, redirect, url_for
from application.forms import LoginForm
from application.models import User, Post
from application import app
from flask_login import logout_user, login_user

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
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        user = User.query.filter_by(username=form.username.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))

        login_user(user, remember=form.remember_me.data)

        return redirect('/Index')

    return render_template('login.html', title='Sign In', form=form)




