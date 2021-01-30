import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"


class Pokedex:
    def fetch_pokemon(self, name):
        response = requests.get(BASE_URL + name).json()

        description = response["flavor_text_entries"][0]["flavor_text"]

        return Pokemon(response["name"])


class Pokemon:
    def __init__(self, name):
        self.name = name
