from flask_login import login_required
from app import app
from flask import render_template
import requests as r
# from .services import 
#need to import any services work here, so the routes know about them!


@app.route('/')
def home():
    greeting = 'Hello Foxes'
    return render_template('index.html',greeting = greeting)

@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/players')
@login_required
def players():
    data = r.get('<<API>>')
    if data.status_code ==200:
        data = data.json()
    else:
        return 'API CURRENTLY DOWN'
    return render_template('f1.html', data = data)
