import requests

URL = "https://api.funtranslations.com/translate/shakespeare.json"


class Shakespeare:
    def translate(self, text):
        response = requests.post(URL, data={"text": text})

        return response.json()["contents"]["translated"]
