# módulos python
from PySide6.QtCore import QObject
from my_tools import resource_path

# módulos locais
from Include.utils import Crypto

class MainModel(QObject):
    def __init__(self):
        super().__init__()

    #----------------------------------------------------
    # gerais
    version = None # by defaults
    symmetric_key = None # by defaults
    _defaults = None
    cfg_file = None # set by thread init (MainController)
    errorMessage = "UNKNOWN_ERROR"
    user = "USUÁRIO"
    _server = None

    #----------------------------------------------------
    # propriedades
    @property
    def defaults(self) -> dict:
        return self._defaults
    
    @defaults.setter
    def defaults(self, value: dict):
        self._defaults = value
        self.symmetric_key = self._defaults['key']
        self.version = self._defaults['version']

        self.crypto = Crypto(self.symmetric_key)

    def logout(self):
        self.cfg_file["LOGIN"]["remember"] = "False"
        self.cfg_file["LOGIN"]["user"] = "None"
        self.cfg_file["LOGIN"]["password"] = "None"

        self.updateCfgDefault()

    def updateCfgDefault(self, **kwargs):
        if kwargs != {}:
            self.cfg_file.update(**kwargs)

        self._server.setCfgFile(resource_path("Files\default.ini"), cfg=self.cfg_file)
