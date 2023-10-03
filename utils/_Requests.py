from requests.exceptions import ConnectionError
import requests

class Requests:
    def __init__(self):
        self.getDefaults()
    
    @property
    def defaults(self) -> dict:
        return self._defaults
    
    def getDefaults(self) -> dict:
        self._defaults = requests.get("https://cs21003200272e2de86.blob.core.windows.net/unit-controle-financeiro/defaults.json").json()
        return self._defaults