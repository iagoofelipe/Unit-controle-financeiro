# módulos python
from PySide6.QtCore import QObject, Signal
from my_tools import encode

# módulos locais
from controllers.src.Database.main import Database

class Model(QObject):    
    #----------------------------------------------------
    # Signal
    connectionChanged = Signal(bool)
    errorDefined = Signal()
    loginPermission = Signal(bool)
    # remember = Signal(bool)

    #----------------------------------------------------
    # property
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
    
    # @property
    # def rememberMe(self):
    #     return self._rememberMe
    
    #----------------------------------------------------
    # setter
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


    @password.setter
    def password(self, value: str):
        self._password = encode(value, True)


    @permission.setter
    def permission(self, value: bool):
        self._permission = value
        self.loginPermission.emit(value)


    # @rememberMe.setter
    # def rememberMe(self, value: bool):
    #     self._rememberMe = value
    #     self.remember.emit(value)


    def getUsers(self) -> list:
        self.db.connect()
        self.db.set_table("users")
        values = self.db.read()
        self.db.close()
        
        return values
    
    #----------------------------------------------------
    def __init__(self):
        super().__init__()
        self.db = Database()
        
        self._connection = None
        self._msgError = "UNKNOWN_ERROR: Erro desconnhecido"
        
        self._users = self.getUsers()
        self._user = "Usuário"
        self._password = ""

        self._permission = False