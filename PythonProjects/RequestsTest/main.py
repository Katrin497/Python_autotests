import requests

URL ='https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : '9109fc5a245b449c64f6608b3e5c3967'}
body_pokemons = {
    "name": "generate",
    "photo_id": 39
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_pokemons)
print(response.text)


body_name = {
    "pokemon_id": "272730",
    "name": "Kolobok",
    "photo_id": 39
}

response_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)


body_add = {
    "pokemon_id": "272730"
}

response_add = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add)
print(response_add.text)
