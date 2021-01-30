import re
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"


class Pokedex:
    def fetch_pokemon(self, name):
        response = requests.get(BASE_URL + name).json()

        description = response["flavor_text_entries"][0]["flavor_text"]

        cleaned_description = re.sub(re.compile(r'\s+'), ' ', description)
        return Pokemon(response["name"], cleaned_description)


class Pokemon:
    def __init__(self, name, description):
        self.name = name
        self.description = description
