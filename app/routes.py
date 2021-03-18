from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Andrade'}
    posts = [{'author': {'username': 'Andrade'}, 'body':'Olá, Andrade'}, {'author':{'username': 'João'}, 'body':'Olá'}]
    return render_template('index.html', user=user, posts=posts)
