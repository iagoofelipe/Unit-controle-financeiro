# módulos python
from PySide6.QtCore import QObject, Signal
import threading, logging, time

# módulos locais
from Include.utils import Server

class MainModel(QObject):
    #----------------------------------------------------
    # Signal
    initFinished = Signal()

    def __init__(self):
        super().__init__()
        threading.Thread(target=self.thread).start()

    #----------------------------------------------------
    # gerais
    def thread(self):
        logging.debug("MainModel inicializando Server")
        self.server = Server()
        self.requests = self.server.requests
        
        time.sleep(2)
        self.initFinished.emit()

    #----------------------------------------------------
    # propriedades