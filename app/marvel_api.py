from marvel import Marvel
import os
import time
from hashlib import md5
import requests
from requests import get
from datetime import datetime
# from .models import Hero






# CHARACTER_URL = 'http://gateway.marvel.com/v1/public/characters'





timestamp = datetime.now().strftime('%Y-%m-%d%H:%M:%S')
pub_key = #copy from .env
priv_key = #copy from .env


def hash_params():
    hash_md5 = md5()
    hash_md5.update(f'{timestamp}{priv_key}{pub_key}'.encode('utf-8'))
    hashed_params = hash_md5.hexdigest()
    return hashed_params


params = {'ts': timestamp, 'apikey': pub_key, 'hash': hash_params(),'limit':100,'offset':100
}
results = get('https://gateway.marvel.com:443/v1/public/characters', params=params)
newdict={}
data = results.json()
print(data['status'])
for hero in data['data']['results']:
    if len(hero['name']) > 39:
        print(hero['name'])
        continue
    if len(hero['description']) >400:
        print (hero['name']+": \n"+hero['description'])
        continue
    
    newdict[hero['name']] = {'name': hero['name'],
                                    'api_id':hero['id'],
                                    'image':hero['thumbnail']['path']+'.'+hero['thumbnail']['extension'],
                                    'description':hero['description']}
print(newdict)













# public_key = 'a04e50bf6e1c9cb8ffce7c7abcb34d32'
# private_key=os.environ.get('MARVEL_KEY')
# m=Marvel('a04e50bf6e1c9cb8ffce7c7abcb34d32','cdb4b90c37d67520dc529568b92fd579983b1ef2')
# character=m.characters
# print (character)
# def character_import():   
#     char_dict = {}
#     all_character=character.all()
#     for hero in all_character['data']['results']:
#         char_dict[hero['name']] = {'name': hero['name'],
#                                     'api_id':hero['id'],
#                                     'image':hero['thumbnail']['path']+'.'+hero['thumbnail']['extension'],
#                                     'description':hero['description']
#         }

#     print (char_dict)

# character_import()
