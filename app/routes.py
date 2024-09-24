from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Liz'}
    return render_template('index.html', title='DAM System Analyzer', user=user)