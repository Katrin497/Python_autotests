import requests
import pytest

URL ='https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '9109fc5a245b449c64f6608b3e5c3967'}
TRAINER_ID = '23242'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['trainer_name'] == 'Катрин'