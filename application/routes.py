from flask import Flask, render_template, flash, redirect
from application.forms import LoginForm
from application import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'moto'}
    posts = [
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },
        {
            'title': {'main': 'I love Python', 'sub': 'this is a happy story'},
            'body': 'Python can do every thing. However, it is very easy.'
        },
        {
            'title': {'main': 'I hate Python', 'sub': 'this is a sad story'},
            'body': 'Python can do every thing. However, it is very hard.'
        },

        {
            'title': {'main': 'I love C#', 'sub': 'this is a happy story'},
            'body': 'C# can do every thing. However, it is very easy.'
        }
    ]

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

    return render_template('login.html', title='Sign In', form=form)


