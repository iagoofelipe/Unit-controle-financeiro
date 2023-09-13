# módulos python
from typing import Optional
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, QObject

# módulos locais
from .ui import *
from .VLogin import LoginView
from .VIniciar import IniciarView
from .VConfig import ConfigView

from .VMatriculas import MatriculasView
from model.model import Model
from controllers.main import MainController
from .app import App

class MainView(QMainWindow):
    def __init__(self, model: Model, main_controller: MainController):
        super().__init__()
        
        self._model = model
        self._main_controller = main_controller
        self.timer = QTimer(self)
        self.uis = dict(Error=self.makeUi(Ui_Error), Matriculas=MatriculasView)
        self.lastUi = LoginView # variável de controle para a ui em processo, sem erros como Model.ui
        
        self._main_controller._view = self
        self._model._view = self

        self._ui = IniciarView(self)
        self._ui.setupUi(self)

        self.timer.timeout.connect(self._main_controller.check_connection)
        self.timer.start(2000)

        # atribuindo métodos de model
        self._model.errorDefined.connect(self._main_controller.on_errorDefined)
        self._model.uiChanged.connect(self._main_controller.on_uiChanged)
        self._model.connectionChanged.connect(self._main_controller.on_connectionChanged)



    def makeUi(self, ui):
        """ retorna QObject da UI informada """
        class Ui(QMainWindow, ui):
            def __init__(self):
                super(Ui, self).__init__()
                self.setupUi(self)

        return Ui
    

    def setUi(self, objectName, start=False):
        if start:
            ui = self.uis[objectName](self._ui)
        else:
            ui = self.uis[objectName]
        
        
        try:
            self._ui.close()
        except AttributeError:
            self.close()
            
        self._ui = ui
        self._ui.setupUi(self._ui)
        self._ui.show()
        # self._model.ui = ui