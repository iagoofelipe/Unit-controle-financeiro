# módulos python
from PySide6.QtWidgets import QMainWindow, QComboBox
from PySide6.QtCore import Slot, QTimer
from typing import Iterable

# módulos locais
from .ui import *
from .Login import Login
from .Matriculas_view import Matriculas_view
from model.model import Model
from controllers.main_ctrl import MainController
from .app import App

class MainView(QMainWindow, App):
    def __init__(self, model: Model, main_controller: MainController):
        super().__init__()
        # atributos iniciais
        self.timer = QTimer(self)
        self._model = model
        self._main_controller = main_controller
        self._ui_atual = dict(ui=Ui_Carregando, objectName="Carregando")
        
        self.changeUi(**self._ui_atual)
        
        # atribuindo métodos de model
        self._model.connectionChanged.connect(self.on_connectionChanged)
        self._model.errorDefined.connect(self.on_errorDefined)
        self._model.loginPermission.connect(self.on_loginPermission)
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
    # métodos on_model
    @Slot(bool)
    def on_connectionChanged(self, value):
        objectName = self.objectName()

        if objectName == "Carregando" and value:
                self._ui.label_processo.setText("êxito na conexão!")
                self._ui_atual = dict(ui=Ui_Login, objectName="Login")
                self.timer.singleShot(2000, lambda: self.changeUi(**self._ui_atual))

        if objectName != "Carregando" and value:
            self._ui_atual = dict(ui=Ui_Login, objectName="Login")
            self.changeUi(**self._ui_atual)


    @Slot()
    def on_errorDefined(self):
         self.changeUi(Ui_Error, "Error")
         self._ui.msg.setText(self._model.msgError)

    
    @Slot(bool)
    def on_loginPermission(self, value):
        if value:
            self.changeUi(objectName="Matriculas")
        else:            
            self._ui.showPopup()

    #-------------------------------------------------------------------------------
    # outros métodos    
    def changeUi(self, ui=None, objectName=None):
        start = True
        match objectName:
            case "Login":
                self._ui = Login(self)
                
            case "Matriculas":
                self._ui = Matriculas_view(self)
            
            case _:
                self._ui = ui()
                start = False

        self.timer.stop()
        self._ui.setupUi(self)
        self.setObjectName(objectName)

        self._ui_atual["objectName"] = objectName
        self._ui_atual["ui"] = self._ui
        
        if start:
            self._ui.start()
    #-------------------------------------------------------------------------------