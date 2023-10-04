# módulos python
from typing import Optional
from PySide6.QtCore import QObject, Slot, Signal
from PySide6.QtWidgets import QMainWindow
import logging, threading, logging, time
from my_tools import resource_path

# módulos locais
from Include.utils import Server

class MainController(QObject):
    initFinished = Signal()
    
    @Slot()
    def on_initFinished(self):
        logging.info("intial connection finished")
        print(self._main_model.defaults)

    def thread(self):
        logging.debug("MainModel inicializando Server")
        self._server = Server()
        self._requests = self._server.requests
        self._main_model.defaults = self._requests.defaults
        self._main_model.cfg_file = self._server.getCfgFile(resource_path("Files\default.ini"))
        
        time.sleep(2)
        self.initFinished.emit()

    def __init__(self, main_model):
        super().__init__()
        self._main_model = main_model
        threading.Thread(target=self.thread).start()
