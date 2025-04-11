import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '131e0b50c73317d064ca381e0c79376e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_change = {
    "pokemon_id": "12331",
    "name": "New Name",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "9"
}

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_create = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_create.text)

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_create.text)