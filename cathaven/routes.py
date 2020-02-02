from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Pinkie'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Nice cats!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'Such a wonderful cats!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)