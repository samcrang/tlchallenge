import pytest
import json
from tlchallenge.app import app


@pytest.fixture()
def fake_charizard_response():
    with open("tests/data/charizard.json") as f:
        return json.loads(f.read())


@pytest.fixture()
def fake_charizard_translation_response():
    with open("tests/data/translation.json") as f:
        return json.loads(f.read())


@pytest.fixture()
def client():
    with app.test_client() as client:
        yield client
