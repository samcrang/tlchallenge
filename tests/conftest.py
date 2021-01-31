import pytest
import json


@pytest.fixture()
def fake_charizard_response():
    with open("tests/data/charizard.json") as f:
        return json.loads(f.read())


@pytest.fixture()
def fake_charizard_translation_response():
    with open("tests/data/translation.json") as f:
        return json.loads(f.read())
