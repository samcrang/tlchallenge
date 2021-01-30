import re
import requests

BASE_URL = "https://pokeapi.co/api/v2/pokemon-species/"


class Pokedex:
    def fetch_pokemon(self, name):
        response = requests.get(BASE_URL + name)

        if response.status_code == 404:
            raise PokemonNotFoundError()

        if response.status_code >= 400:
            raise PokeapiError()

        json = response.json()

        description = None
        for entry in reversed(json["flavor_text_entries"]):
            if (
                entry["language"]["name"] == "en"
                and entry["version"]["name"] == "alpha-sapphire"
            ):
                description = entry["flavor_text"]
                break

        if description is None:
            for entry in reversed(json["flavor_text_entries"]):
                if entry["language"]["name"] == "en":
                    description = entry["flavor_text"]
                    break

        return Pokemon(json["name"], self.__clean(description))

    def __clean(self, string):
        return re.sub(re.compile(r"\s+"), " ", string)


class Pokemon:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class PokemonNotFoundError(Exception):
    pass


class PokeapiError(Exception):
    pass
