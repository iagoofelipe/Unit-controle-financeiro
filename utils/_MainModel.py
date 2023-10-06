# módulos python
from PySide6.QtCore import QObject
import logging, configparser, os

# módulos locais
from static import PATH_CFG_DEFAULT

class MainModel(QObject):
    database = None # set by ControllerIniciar
    requests = None # set by ControllerIniciar
    crypto = None # set by ControllerIniciar
    username = None # set by ControllerLogin
    errorMessage = "UNDEFINED_ERROR"

    def __init__(self):
        super().__init__()
        self._cfg_default = self.getCfgFile(PATH_CFG_DEFAULT)

    @property
    def cfg_default(self):
        return self._cfg_default
    
    @cfg_default.setter
    def cfg_default(self, value):
        self.setCfgFile(PATH_CFG_DEFAULT, **value)
        self._cfg_default = self.getCfgFile(PATH_CFG_DEFAULT)

    @staticmethod
    def setCfgFile(file: str, **kwargs) -> None:
        if 'cfg' in kwargs:
            config = kwargs['cfg']

        else:        
            if not os.path.exists(file):
                with open(file, 'w') as f:
                    f.write('')

            config = __class__.getCfgFile(file)
            for key, value in kwargs.items():
                config[key].update(value)

        with open(file, 'w') as cfg:
            config.write(cfg)        

    @staticmethod
    def getCfgFile(fileName) -> configparser.ConfigParser:
        config = configparser.ConfigParser()
        config.read(fileName)
        return config