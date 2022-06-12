from distutils.command.upload import upload
from flask import Blueprint, jsonify,request
from flask_login import current_user
from app.models import db, Hero
from .services import token_required

api= Blueprint('api',__name__,url_prefix='/api')

# #initial testing route
@api.route('/test', methods=['GET'])
def test():
    return jsonify('testing'),200


#the purpose of this API is going to be to hold a database of Marvel Characters in users 'CART'

@api.route('/heroes',methods=['GET'])
def getHeros():
    heroes= Hero.query.all()
    heroes=[a.to_dict() for a in heroes]#list comprehension version
    #heroes={a.species: a.to_dict() for a in heroes}#dictionary comprehension version
    return jsonify(heroes)

@api.route('/add',methods=["POST"])
@token_required
def createHero():
    try:   
        newdict = request.get_json()        
        h=Hero(newdict)
    except:
        return jsonify({'error':'improper request or body data'}),400
    try:
        db.session.add(h)
        db.session.commit()
    except:
        return jsonify({'error':'Hero already exists in the database'}),400
    return jsonify({'created':h.to_dict()}),200

@api.route('/hero/<string:name>',methods = ['GET'])
def getHeroName(name):
    """
    [GET] retrieving a single hero from the database based on that heroes name
    so we will get an hero name in from the dynamic route URL,
    query the db for that hero, and return if it exists
    """
    print(name)

    hero = Hero.query.filter_by(name=name.title()).first()
    if hero:
        return jsonify(hero.to_dict()), 200
    #otherwise return an error message
    return jsonify({'error':f'The name {name.title()} does not exist in the database.'}),400

@api.route('/update/<string:id>',methods= ['POST'])
#@token_required
def updateHero(id): 
    try:
        newvals = request.get_json()
        print(1)
        hero=Hero.query.get(id)
        print(2)
        hero.from_dict(newvals)
        print(3)
        db.session.commit()
        print(4)
        return jsonify({'Updated Hero': hero.to_dict()})
    except:
        return jsonify({'Request failed':'Invalid request or hero ID does not exist.'}),400   

@api.route('/delete/<string:id>', methods=['DELETE'])
#@token_required
def removeHero(id):
    """
    [DELETE]  accepts a hero ID - if that ID exists in the database, remove that hero and return the removed hero object
    """

    hero = Hero.query.get(id)
    if not hero:
        return jsonify({'Remove Failed': f'No hero with ID {id} in the database.'}), 404
    db.session.delete(hero)
    db.session.commit()
    return jsonify({'Removed hero': hero.to_dict()}),200


@api.route('/upload', methods = ['GET','POST'])
def upload_Heroes():
    
    
    x=()
    for i in x:
        y=Hero(x[i],userid=current_user.id)
        db.session.add(y)
    db.session.commit()
    return jsonify('Added heroes'),200
