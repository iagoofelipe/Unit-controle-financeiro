# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import logging

# módulos locais
from src.uis import Ui_Home
from .controller import ControllerHome
from .model import ModelHome
from static import WINDOW_TITLE
# from ._Registros import Registros
from .Registros import ViewRegistros
from utils._App import App

class ViewHome(QObject, Ui_Home, App):
    def __init__(self, mainView):
        super(ViewHome, self).__init__()
        self.setupUi(mainView)
        
        # atributos gerais
        self._main_view = mainView
        self._main_model = mainView._main_model
        self._main_controller = mainView._main_controller

        # atributos privados
        self._timer = QTimer()
        self._model = ModelHome(self)
        self._controller = ControllerHome(self)
        
        # métodos privados
        self._main_view.setWindowTitle(WINDOW_TITLE)

        # sinais e slots
        self._controller.threadFinished.connect(self.on_threadFinished)

        # camadas do módulo atual
        self._registros = ViewRegistros(self)

    @Slot(dict)
    def on_threadFinished(self, values: dict):
        """ thread inicial da interface """