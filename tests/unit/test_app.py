from unittest.mock import patch

from tlchallenge.pokedex import Pokemon


@patch("tlchallenge.app.Shakespeare")
@patch("tlchallenge.app.Pokedex")
def test_returns_description_translation(fake_pokedex, fake_shakespeare, client):
    fake_pokedex.return_value.fetch_pokemon.return_value = Pokemon(
        "charizard", "charizard description"
    )

    fake_shakespeare.return_value.translate.return_value = (
        "translated charizard description"
    )

    response = client.get("/pokemon/charizard").json

    assert response["name"] == "charizard"
    assert response["description"] == "translated charizard description"
