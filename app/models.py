from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
from flask_login import LoginManager,UserMixin
login=LoginManager()
from datetime import datetime
from uuid import uuid4
from werkzeug.security import generate_password_hash
# Create a DB model
login=LoginManager()

@login.user_loader
def load_user(userid):
    return User.query.get(userid)


class User(db.Model, UserMixin):
    id = db.Column(db.String(40),primary_key=True)
    username=db.Column(db.String(60), nullable = False, unique = True)
    email=db.Column(db.String(100), nullable = False, unique = True)
    password= db.Column(db.String(255),nullable=False)
    bio=db.Column(db.String(255),default='No bio.')
    first_name=db.Column(db.String(100))
    last_name=db.Column(db.String(100))
    created= db.Column(db.DateTime, default = datetime.now())#not needed in init because of default value.
    api_token = db.Column(db.String(100))
    heroes = db.relationship('Hero', backref='hero_userid')

    def __init__(self,username,email,password,first_name,last_name):
        self.username = username
        self.email = email.lower()
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.id = str(uuid4())#UUID is a UUID object, not string. Need to convert.
        self.password = generate_password_hash(password)


class Hero(db.Model):
    id =db.Column(db.String(40), primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    description = db.Column(db.String(400))
    image=db.Column(db.String(150))
    api_id=db.Column(db.Integer)
    userid = db.Column(db.String(80),db.ForeignKey('user.id'))

    def __init__(self,dict,userid):
        self.id=str(uuid4())
        self.name=dict['name'].title()
        self.description = dict['description']
        self.image=dict.get('image')
        self.api_id=dict['api_id']
        self.userid = userid


    #write a function to translate this object to a dictionary for jsonification
    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'description':self.description,
            'image':self.image,
            'api_id':self.api_id
        }

        #need from-dict here
    def from_dict(self, dict):
        for key in dict:
            getattr(self, key)
            setattr(self, key, dict[key])