from tlchallenge.pokedex import Pokedex


def test_returns_name_and_description_for_a_pokemon():
    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.name == "charizard"
