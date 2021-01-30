import pytest
import json


@pytest.fixture()
def fake_charizard_response():
    with open("tests/data/charizard.json") as f:
        return json.loads(f.readlines()[0])
