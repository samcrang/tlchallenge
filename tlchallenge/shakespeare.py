import re
import requests

URL = "https://api.funtranslations.com/translate/shakespeare.json"


class Shakespeare:
    def translate(self, text):
        response = requests.post(URL, data={"text": text})

        if response.status_code >= 400:
            raise ShakespeareAPIError()

        return self.__clean(response.json()["contents"]["translated"])

    def __clean(self, string):
        return re.sub(re.compile(r"\s+"), " ", string)


class ShakespeareAPIError(Exception):
    pass
