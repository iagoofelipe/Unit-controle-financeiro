# módulos python
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow
from my_tools import encode, File, resource_path

# módulos locais
from controllers.src import Database, Crypto

class Model(QObject):    
    #----------------------------------------------------
    # Signal
    uiChanged = Signal(object)
    connectionChanged = Signal(bool)
    errorDefined = Signal()
    # logout = Signal(object)


    # #----------------------------------------------------
    # # property
    @property
    def ui(self):
        return self._ui
    
    @property
    def msgError(self):
        return self._msgError
    
    @property
    def connection(self):
        return self._connection
    

    

    

    
    # #----------------------------------------------------
    # setter
    @ui.setter
    def ui(self, __obj: QMainWindow | QObject):
        self._ui = __obj
        
        if type(self._view._ui) == QMainWindow:
            geometry = self._view._ui.geometry()
        else:
            geometry = self._view.geometry()    

        self._view._ui = self._ui

        self._view.close()
        self._view.timer.stop()
        
        self._ui.show()
        self._ui.setGeometry(geometry)
        # self.uiChanged.emit(__obj)


    @msgError.setter
    def msgError(self, value: str):
        self._msgError = value
        self.errorDefined.emit()

    
    @connection.setter
    def connection(self, value: bool):
        # em caso de queda na conexão
        if value != self._connection:
            self._connection = value
            self.connectionChanged.emit(value)


    def getUsers(self) -> list:
        try:
            self.db.set_table("users")
            values = self.db.read()
        except:
            values = []
            
        return values
    
    #----------------------------------------------------
    def __init__(self):
        super().__init__()
        from . import MatriculasModel
        from . import LoginModel
        
        self.db = Database()
        self.json_const = File.getFile(resource_path("model/Files/const.json"))
        # self.crypto.key = self.json_const["key"]

        self._connection = None
        # self._msgError = "UNKNOWN_ERROR: Erro desconnhecido"
        
        self._users = self.getUsers()
        # self._user = self.json_const["login"]["user"]
        # self._password = self.crypto.decode(self.json_const["login"]["password"])

        # self._windowTitle = self.json_const["windowTitle"]
        
        # self.matriculas = MatriculasModel()
        # self.login = LoginModel(self)