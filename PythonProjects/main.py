"""
PythonProjects test api
"""
import requests

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json','trainer_token' : 'dd7f5f9868cae4ccc5975be83f0c8692'}

body = {
    "name": "Огонь",
    "photo": "https://dolnikov.ru/pokemons/albums/014.png"
}


response = requests.post(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')



URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json','trainer_token' : 'dd7f5f9868cae4ccc5975be83f0c8692'}

body = {
    "pokemon_id": "28497",
    "name": "Человечек",
    "photo": "https://dolnikov.ru/pokemons/albums/005.png"
}

response = requests.put(url=f'{URL}/pokemons', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')




URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json','trainer_token' : 'dd7f5f9868cae4ccc5975be83f0c8692'}

body = {
    "pokemon_id": "28497",
}

response = requests.post(url=f'{URL}/trainers/add_pokeball', json=body, headers=HEADER)
print(f'Статус код: {response.status_code}. Сообщение: {response.json()["message"]}')