# módulos python
from PySide6.QtCore import QObject

# módulos locais
from resources.uis import Ui_Config
from .app import App

class ConfigController(QObject):
    def __init__(self, view):
        super(ConfigController, self).__init__()
        # self._model = mainView._model
        self._view = view


class VConfig(QObject, Ui_Config, App):
    def __init__(self, mainView):
        super(VConfig, self).__init__()
        self.setupUi(mainView)
        
        # self.timer = mainView._child_timer
        self._main_model = mainView._main_model
        self._main_view = mainView
        self._controller = ConfigController(self)
        self.json_const = self._main_model.json_const
        
        self.setTimer("VConfig")
        self.btn_cancelar.clicked.connect(self.btnCancelarAction)
        self.btn_aplicar.clicked.connect(self.setJsonValues)
        
        self.getValues()
        self.timeout.setValue(self._timeout)
        self.regTable_lengh.setValue(self._regTable_lengh)
    
    def btnCancelarAction(self):
        self._main_view.setUi("Matriculas")

    # def start(self):
    #     """ funções executadas com timer """
    #     print("VConfig")

    def getValues(self):
        self._timeout = self.json_const["timeout"]
        self._regTable_lengh = self.json_const["regTable_lengh"]

    def setJsonValues(self):
        self._timeout = int(self.timeout.text())
        self._regTable_lengh = int(self.regTable_lengh.text())
        
        self.json_const["timeout"] = self._timeout
        self.json_const["regTable_lengh"] = self._regTable_lengh
        
        self._main_model.setJsonConst(self.json_const)