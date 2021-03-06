import pytest
import responses

from tlchallenge.shakespeare import Shakespeare, ShakespeareAPIError, URL


@responses.activate
def test_translates_given_text_to_shakespeare(fake_charizard_translation_response):
    description = "Charizard flies around the sky in search of powerful opponents. It breathes fire of such great heat that it melts anything. However, it never turns its fiery breath on any opponent weaker than itself."
    responses.add(
        responses.POST,
        URL,
        match=[responses.urlencoded_params_matcher({"text": description})],
        json=fake_charizard_translation_response,
        status=200,
    )

    client = Shakespeare()

    assert (
        client.translate(description)
        == "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However, 't nev'r turns its fiery breath on any opponent weaker than itself."
    )


@responses.activate
@pytest.mark.parametrize("status", [400, 401, 500, 501])
def test_throws_if_shakespeare_api_returns_non_successful_response(status):
    responses.add(
        responses.POST,
        URL,
        match=[responses.urlencoded_params_matcher({"text": "foo"})],
        status=status,
    )

    with pytest.raises(ShakespeareAPIError):
        Shakespeare().translate("foo")
