import re
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"


class Pokedex:
    def fetch_pokemon(self, name):
        response = requests.get(BASE_URL + name).json()

        description = None
        for entry in reversed(response["flavor_text_entries"]):
            if (
                entry["language"]["name"] == "en"
                and entry["version"]["name"] == "alpha-sapphire"
            ):
                description = entry["flavor_text"]
                break

        if description is None:
            for entry in reversed(response["flavor_text_entries"]):
                if entry["language"]["name"] == "en":
                    description = entry["flavor_text"]
                    break

        return Pokemon(response["name"], self.__clean(description))

    def __clean(self, string):
        return re.sub(re.compile(r"\s+"), " ", string)


class Pokemon:
    def __init__(self, name, description):
        self.name = name
        self.description = description
