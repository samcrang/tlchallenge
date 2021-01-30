# Pokemon Challenge

## Setup

```
virtualenv --python=python3.8 .venv
brew install httpie
pip install -r requirements.txt
```

## Running

```
FLASK_APP="tlchallenge/app.py" FLASK_ENV=development flask run
```

## Tests

```
python -m pytest
python -m pytest tests/unit
python -m pytest tests/integration
python -m pytest tests/acceptance
```
