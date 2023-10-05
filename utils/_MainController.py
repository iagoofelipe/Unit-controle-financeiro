# módulos python
from PySide6.QtCore import QObject, Signal, Slot

# módulos locais

class MainController(QObject):
    database = None # set by ControllerIniciar
    requests = None # set by ControllerIniciar
    crypto = None # set by ControllerIniciar
    
    def __init__(self, main_model):
        super().__init__()