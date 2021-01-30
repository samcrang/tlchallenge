from tlchallenge.pokedex import Pokedex


def test_returns_name_and_description_for_a_pokemon():
    pokedex = Pokedex()
    charizard = pokedex.fetch_pokemon("charizard")

    assert charizard.name == "charizard"
    assert (
        charizard.description
        == "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself."
    )
