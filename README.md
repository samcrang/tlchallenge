# Pokemon Challenge

Translates a Pokemon description into Shakespeare. Uses an English description but prefers the `alpha-sapphire` description.

## Setup

```
brew install httpie
virtualenv --python=python3.8 .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Tests

Run unit tests using stubbed API responses:

```
python -m pytest tests/unit
```

Run integration tests using external services:

```
python -m pytest tests/integration
```

Run acceptance tests. Requires a running instance on `127.0.0.1:5000`:

```
python -m pytest tests/acceptance
```

Run all the tests:

```
python -m pytest
```

## Running

```
FLASK_APP="tlchallenge/app.py" FLASK_ENV=development flask run

# or

docker build .
docker run -p 5000:5000 <image id>
```
