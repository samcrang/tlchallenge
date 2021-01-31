from flask import Flask, jsonify

from tlchallenge.pokedex import Pokedex
from tlchallenge.shakespeare import Shakespeare


app = Flask(__name__)


@app.route("/pokemon/<name>")
def shakespearify_pokemon_description(name):
    pokedex = Pokedex()
    shakespeare = Shakespeare()

    pokemon = pokedex.fetch_pokemon(name)
    translation = shakespeare.translate(pokemon.description)

    return jsonify({"name": pokemon.name, "description": translation})
