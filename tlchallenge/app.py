from flask import Flask, jsonify, abort

from tlchallenge.pokedex import Pokedex, PokemonNotFoundError
from tlchallenge.shakespeare import Shakespeare


app = Flask(__name__)


@app.route("/pokemon/<name>")
def shakespearify_pokemon_description(name):
    pokedex = Pokedex()
    shakespeare = Shakespeare()

    try:
        pokemon = pokedex.fetch_pokemon(name)
    except PokemonNotFoundError:
        abort(404)

    translation = shakespeare.translate(pokemon.description)

    return jsonify({"name": pokemon.name, "description": translation})
