from flask_login import login_required,current_user
from app import app
from flask import render_template
import requests as r

#need to import any services work here, so the routes know about them!
from .models import User, Hero,db

@app.route('/')
def home():
    if current_user:
        print(current_user)
    return render_template('index.html')

@app.route('/about')
def about():    
    return render_template('about.html')

@app.route('/profile/<string:username>',methods = ['GET'])
def profile(username):
    user = User.query.filter_by(username=username)
    if user:
        heroes = Hero.query.filter_by(userid = user.id).all()
        return render_template('profile.html',user=user,heroes=heroes)
    
    else:
        return 'This isnt a user'
    
