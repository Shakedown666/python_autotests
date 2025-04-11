import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '131e0b50c73317d064ca381e0c79376e'
HEADER = {'Content-Type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = '28635'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID}) 
    assert response_get.json()["data"][0]["id"] == '28635'
