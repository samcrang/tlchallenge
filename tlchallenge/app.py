from flask import Flask, jsonify


app = Flask(__name__)


@app.route("/pokemon/<name>")
def shakespearify_pokemon_description(name):
    pass
