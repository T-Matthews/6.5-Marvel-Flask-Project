from flask import Blueprint, jsonify

api= Blueprint('api',__name___prefix='/api')
from app.models import Hero

#initial testing route
@api.route('/test', metods=['GET'])
def test():
    
    return jsonify('testing'),200


#the purpose of this API is going to be to hold a database of Marvel Characters in users 'CART'

