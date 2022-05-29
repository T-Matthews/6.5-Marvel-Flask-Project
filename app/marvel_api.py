from marvel import Marvel
import os

public_key = 'a04e50bf6e1c9cb8ffce7c7abcb34d32'
private_key=os.environ.get('MARVEL_KEY')
m=Marvel(public_key,private_key)
character=m.characters
char_dict = {}
all_character=character.all()
for hero in all_character['data']['results']:
    char_dict[hero['name']] = {'name': hero['name'],
                                'alt_id':hero['id'],
                                'thumbnail':hero['thumbnail']['path']+hero['thumbnail']['extension'],
                                'description':hero['description']
    }

print (char_dict)

