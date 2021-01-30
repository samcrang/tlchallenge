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
                {
                    "flavor_text": "something \nsomething\u000csomething.",
                    "language": {"name": "en"},
                    "version": {"name": "yellow"},
                }
            ],
        },
        status=200,
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.description == "something something something."


@responses.activate
def test_returns_newest_english_description():
    responses.add(
        responses.GET,
        BASE_URL + "charizard",
        json={
            "name": "charizard",
            "flavor_text_entries": [
                {
                    "flavor_text": "German description",
                    "language": {"name": "de"},
                    "version": {"name": "yellow"},
                },
                {
                    "flavor_text": "English description old",
                    "language": {"name": "en"},
                    "version": {"name": "blue"},
                },
                {
                    "flavor_text": "English description new",
                    "language": {"name": "en"},
                    "version": {"name": "yellow"},
                },
            ],
        },
        status=200,
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.description == "English description new"


@responses.activate
def test_returns_english_alpha_sapphire_description_if_available():
    responses.add(
        responses.GET,
        BASE_URL + "charizard",
        json={
            "name": "charizard",
            "flavor_text_entries": [
                {
                    "flavor_text": "Alpha-Sapphire English description",
                    "language": {"name": "en"},
                    "version": {"name": "alpha-sapphire"},
                },
                {
                    "flavor_text": "Red English description",
                    "language": {"name": "en"},
                    "version": {"name": "red"},
                },
                {
                    "flavor_text": "Alpha-Sapphire German description",
                    "language": {"name": "de"},
                    "version": {"name": "alpha-sapphire"},
                },
            ],
        },
        status=200,
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.description == "Alpha-Sapphire English description"


@responses.activate
def test_returns_name_for_a_pokemon(fake_charizard_response):
    responses.add(
        responses.GET, BASE_URL + "charizard", json=fake_charizard_response, status=200
    )

    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.name == "charizard"
    assert (
        charizard.description
        == "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself."
    )
