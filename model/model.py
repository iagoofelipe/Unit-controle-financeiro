# módulos python
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMainWindow
from my_tools import encode, File, resource_path

# módulos locais
from controllers.src import Database, Crypto
from .Matriculas_model import MatriculasModel

class Model(QObject, MatriculasModel):    
    #----------------------------------------------------
    # Signal
    uiChanged = Signal(tuple)
    connectionChanged = Signal(bool)
    errorDefined = Signal()
    loginPermission = Signal(bool)
    logout = Signal(object)

    crypto = Crypto()

    #----------------------------------------------------
    # property
    @property
    def ui(self):
        return self._ui
    
    @property
    def msgError(self):
        return self._msgError
    
    @property
    def connection(self):
        return self._connection
    
    @property
    def user(self):
        return self._user
    
    @property
    def password(self):
        return self._password
    
    @property
    def permission(self):
        return self._permission
    
    @property
    def remember(self):
        return self._remember
    
    #----------------------------------------------------
    # setter
    def setUi(self, master, __obj: QMainWindow):
        self._ui = __obj
        self.uiChanged.emit((master, __obj))


    @msgError.setter
    def msgError(self, value: str):
        self._msgError = value
        self.errorDefined.emit()

    
    @connection.setter
    def connection(self, value: bool):
        if value != self._connection:
            self._connection = value
            self.connectionChanged.emit(value)


    @user.setter
    def user(self, value: str):
        self._user = encode(value, True)
        self.json_const["login"]["user"] = self._user
        File.toFile(resource_path("model/Files/const.json"), self.json_const)


    @password.setter
    def password(self, value: str):
        self._password = encode(value)
        self.json_const["login"]["password"] = self.crypto.encode(self._password, "str")
        File.toFile(resource_path("model/Files/const.json"), self.json_const)


    @permission.setter
    def permission(self, value: bool):
        self._permission = value
        self.loginPermission.emit(value)


    @remember.setter
    def remember(self, value: bool):
        self._remember = value
        self.json_const["login"]["remember"] = self._remember
        File.toFile(resource_path("model/Files/const.json"), self.json_const)


    def getUsers(self) -> list:
        try:
            self.db.connect()
            self.db.set_table("users")
            values = self.db.read()
            self.db.close()
        except:
            values = []
            
        return values
    
    #----------------------------------------------------
    def __init__(self):
        super().__init__()
        self.db = Database()
        self.json_const = File.getFile(resource_path("model/Files/const.json"))
        self.crypto.key = self.json_const["key"]

        self._connection = None
        self._msgError = "UNKNOWN_ERROR: Erro desconnhecido"
        
        self._users = self.getUsers()
        self._user = self.json_const["login"]["user"]
        self._password = self.crypto.decode(self.json_const["login"]["password"])
        self._remember = self.json_const["login"]["remember"]

        self._permission = False
        self._windowTitle = self.json_const["windowTitle"]