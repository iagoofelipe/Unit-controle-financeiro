# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import logging

# módulos locais
from src.uis import Ui_Name
from .controller import ControllerName
from .model import ModelName

class ViewName(QObject, Ui_Name):
    def __init__(self, mainView):
        super(ViewName, self).__init__()
        self.setupUi(mainView)
        
        # atributos gerais
        self._main_view = mainView
        self._main_model = mainView._main_model
        self._main_controller = mainView._main_controller

        # atributos privados
        self._timer = QTimer()
        self._model = ModelName(self)
        self._controller = ControllerName(self)

        # sinais e slots
        self._controller.threadFinished.connect(self.on_threadFinished)

    @Slot(dict)
    def on_threadFinished(self, values: dict):
        """ thread inicial da interface """