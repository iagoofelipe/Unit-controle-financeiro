# módulos python
from PySide6.QtWidgets import QMainWindow, QComboBox
from PySide6.QtCore import Slot, QTimer
from typing import Iterable

# módulos locais
from .ui import *
from .Login import Login
from .Carregando_view import Carregando_view
from .Config_view import ConfigView

from .Matriculas_view import Matriculas_view
from model.model import Model
from controllers.main import MainController
from .app import App

class MainView(QMainWindow, App):
    def __init__(self, model: Model, main_controller: MainController):
        super().__init__()
        # atributos iniciais
        self.timer = QTimer(self)
        self._model = model
        self._main_controller = main_controller
        self._ui_atual = dict(ui=Carregando_view, objectName="Carregando")
        self.uis = dict(Error=Ui_Error, Login=Login, Matriculas=Matriculas_view, Carregando=Carregando_view, Config=ConfigView)
        self._main_controller.view = self
        
        self.changeUi(**self._ui_atual)
        
        # atribuindo métodos de model
        self._model.connectionChanged.connect(self._main_controller.on_connectionChanged)
        self._model.errorDefined.connect(self._main_controller.on_errorDefined)
        self._model.loginPermission.connect(self._main_controller.on_loginPermission)
        self._model.logout.connect(self._main_controller.on_logout)
        
        # atribuindo métodos de controller
        self.timer.timeout.connect(self._main_controller.check_connection)
        self.timer.start(2000)

        

    def logout(self, master):
        master.timer.stop()

        self.timer.timeout.connect(self._main_controller.check_connection)
        self.timer.start(2000)
        self._model.logout.emit(self)

    #-------------------------------------------------------------------------------
    # outros métodos    
    def changeUi(self, ui=None, objectName=None):
        start = True
        if objectName in ("Login", "Matriculas", "Carregando", "Config"):
            self._ui = self.uis[objectName](self)

        else:
            self._ui = ui()
            start = False

        self.timer.stop()
        self._ui.setupUi(self)
        self.setObjectName(objectName)
        self.setWindowTitle(self._model._windowTitle)

        self._ui_atual["objectName"] = objectName
        self._ui_atual["ui"] = self._ui
        
        if start:
            self._ui.start()
    #-------------------------------------------------------------------------------