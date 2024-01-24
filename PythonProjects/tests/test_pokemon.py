import requests
import pytest

URL = 'https://api.pokemonbattle.me:9104'
HEADER = {'Content-Type':'application/json','trainer_token' : 'dd7f5f9868cae4ccc5975be83f0c8692'}

def test_get_trainers_by_level():
  """
  Get trainers by level
  """

  response = requests.get(url=f'{URL}/trainers', params={'level': 1}, timeout=5)
  assert response.status_code ==200, 'Unexpected status code'


def test_get_trainers_by_id():
  """
  Get trainers by level
  """

  response = requests.get(url=f'{URL}/trainers', params={'trainer_id': 3636}, timeout=5)
  assert response.json()['trainer_name'] == 'Ромэо'