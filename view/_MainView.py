# módulos python
from PySide6.QtWidgets import QMainWindow

# módulos locais
from ._VIniciar import VIniciar

class MainView(QMainWindow):
    def __init__(self, main_model, main_controller):
        super(MainView, self).__init__()
        VIniciar(self)
        
        self._main_model = main_model
        self._main_controller = main_controller

        self._main_model.initFinished.connect(self._main_controller.on_initFinished)
        self._main_model.initFinished.connect(self.v_initFinished)

    def v_initFinished(self):
        pass