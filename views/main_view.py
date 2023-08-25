# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Slot, QTimer

# módulos locais
from .ui import *
from .Login import Login
from .Matriculas import Matriculas
from model.model import Model
from controllers.main_ctrl import MainController

class MainView(QMainWindow):
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
        
        # atribuindo métodos de controller
        self.timer.timeout.connect(self._main_controller.check_connection)
        self.timer.start(2000)

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
                self._ui = Matriculas(self)
            
            case _:
                self._ui = ui()
                start = False

        self._ui.setupUi(self)
        self.setObjectName(objectName)
        
        if start:
            self._ui.start()
        
    #-------------------------------------------------------------------------------