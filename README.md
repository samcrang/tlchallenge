# Pokemon Challenge

## Setup

```
virtualenv --python=python3.8 .venv
brew install httpie
pip install -r requirements.txt
```

## Tests

```
python -m pytest
python -m pytest tests/unit
python -m pytest tests/integration
```

The following requires a running instance of the app:

```
python -m pytest tests/acceptance
```

## Running

```
FLASK_APP="tlchallenge/app.py" FLASK_ENV=development flask run

# or

docker build .
docker run -p 5000:5000 <image id>
```
