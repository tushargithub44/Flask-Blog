from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Tushar'}
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
    return render_template('index.html',title = "Home", user = user, posts = posts)
