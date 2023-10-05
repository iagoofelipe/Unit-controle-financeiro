# módulos python
from PySide6.QtCore import QObject, Signal
from threading import Thread
from my_tools import resource_path
import logging, time

# módulos locais
from utils import Database, Requests, Crypto, Server

class ControllerIniciar(QObject):
    threadFinished = Signal(dict)

    def __init__(self, view):
        super().__init__()
        
        # atributos gerais
        self._view = view
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        # inicializando thread
        Thread(target=self.on_thread).start()

    def on_thread(self):
        """ definindo atributos gerais durante inicialização do programa """
        logging.debug("incializando thread INICIAL")
        self._main_controller.database = self._main_model.database = Database()
        self._main_controller.requests = self._main_model.requests = Requests()
        self._main_controller.crypto = self._main_model.crypto = Crypto(self._main_model.requests.defaults['key'])
        # self._main_controller.cfg_default = self._main_model.cfg_default = Server.getCfgFile(resource_path("default.ini"))

        # em caso de erro
        if not self._main_model.database.test_connection():
            
            self.threadFinished.emit(dict(fail=True, error="DATABASE_ERROR: não foi possível conectar se ao banco de dados"))
            return
        
        if self._main_model.requests.fail:
            self.threadFinished.emit(dict(fail=True, error="REQUESTS_ERROR: não foi possível conectar se ao servidor"))
            return

        self.threadFinished.emit(dict(fail=False))