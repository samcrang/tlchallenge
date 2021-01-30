from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/pokemon/<name>")
def shakespearify_pokemon_description(name):
    return jsonify(
        {
            "name": "charizard",
            "description": "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However, 't nev'r turns its fiery breath on any opponent weaker than itself.",
        }
    )
