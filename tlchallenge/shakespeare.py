import requests

URL = "https://api.funtranslations.com/translate/shakespeare.json"


class Shakespeare:
    def translate(self, text):
        response = requests.post(URL, data={"text": text})

        if response.status_code >= 400:
            raise ShakespeareAPIError()

        return response.json()["contents"]["translated"]


class ShakespeareAPIError(Exception):
    pass
