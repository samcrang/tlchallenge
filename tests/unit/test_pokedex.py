import responses

from tlchallenge.pokedex import Pokedex, BASE_URL


@responses.activate
def test_strips_whitespace_from_pokemon_description():
    responses.add(
        responses.GET,
        BASE_URL + "charizard",
        json={
            "name": "charizard",
            "flavor_text_entries": [
                {"flavor_text": "something \nsomething\u000csomething."}
            ],
        },
        status=200,
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.description == "something something something."


@responses.activate
def test_returns_name_for_a_pokemon(fake_charizard_response):
    responses.add(
        responses.GET, BASE_URL + "charizard", json=fake_charizard_response, status=200
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.name == "charizard"
