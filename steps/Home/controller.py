# módulos python
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread

# módulos locais

class ControllerHome(QObject):
    threadFinished = Signal()

    def __init__(self, view):
        super().__init__()
        
        # atributos gerais
        self._view = view
        self._model = view._model
        
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        # inicializando thread
        Thread(target=self.on_thread).start()

    @Slot()
    def on_thread(self):
        """ definindo atributos gerais durante inicialização da classe """