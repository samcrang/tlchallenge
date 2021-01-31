from tlchallenge.shakespeare import Shakespeare


def test_translates_given_text_to_shakespeare():
    client = Shakespeare()

    translation = client.translate(
        "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself."
    )

    assert (
        translation
        == "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However, 't nev'r turns its fiery breath on any opponent weaker than itself."
    )
