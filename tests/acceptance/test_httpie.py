import subprocess
import json


def test_acceptance():
    result = subprocess.run(
        "http GET http://localhost:5000/pokemon/charizard",
        shell=True,
        capture_output=True,
    )

    response = json.loads(result.stdout)

    assert response["name"] == "charizard"
    assert (
        response["description"]
        == "Charizard flies 'round the sky in search of powerful opponents. 't breathes fire of such most wondrous heat yond 't melts aught. However, 't nev'r turns its fiery breath on any opponent weaker than itself."
    )
