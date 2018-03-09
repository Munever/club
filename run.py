from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = {'username': 'Minever'}
    post = []
    return render_template('index.html', post=post, user=user)


app.run()

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
    return render_template('index.html', items=items)

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

app.run()