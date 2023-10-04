# módulos python
from PySide6.QtCore import QObject, Signal
import threading, logging, time

# módulos locais
from Include.utils import Crypto

class MainModel(QObject):
    #----------------------------------------------------
    # Signal

    def __init__(self):
        super().__init__()

    #----------------------------------------------------
    # gerais
    version = None # by defaults
    symmetric_key = None # by defaults
    _defaults = None
    cfg_file = None # set by thread init
    errorMessage = "UNKNOWN_ERROR"

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