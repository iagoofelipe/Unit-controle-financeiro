from PySide6.QtCore import QObject, Signal
from my_tools import File, resource_path, encode
from controllers.src import Crypto

class LoginModel(QObject):
    loginPermission = Signal(bool)
    crypto = Crypto()
    
    @property
    def remember(self):
        return self._remember
    
    @remember.setter
    def remember(self, value: bool):
        self._remember = value
        self.json_const["login"]["remember"] = self._remember
        File.toFile(resource_path("model/Files/const.json"), self.json_const)


    @property
    def permission(self):
        return self._permission

    @permission.setter
    def permission(self, value: bool):
        self._permission = value
        self.loginPermission.emit(value)  


    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value: str):
        self._user = encode(value, True)
        self.json_const["login"]["user"] = self._user
        File.toFile(resource_path("model/Files/const.json"), self.json_const)


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value: str):
        self._password = encode(value)
        self.json_const["login"]["password"] = self.crypto.encode(self._password, "str")
        File.toFile(resource_path("model/Files/const.json"), self.json_const)

    #----------------------------------------------------
    def __init__(self, master):
        super().__init__()
        from . import Model

        self._model: Model = master._main_model

        # self.db = Database()
        self.json_const = self._model.json_const
        self.crypto.key = self.json_const["key"]

        self._connection = None
        # self._msgError = "UNKNOWN_ERROR: Erro desconnhecido"
        
        self._users = self._model.getUsers()
        self._user = self.json_const["login"]["user"]
        self._password = self.crypto.decode(self.json_const["login"]["password"])
        self._remember = self.json_const["login"]["remember"]

        self._permission = False
        self._windowTitle = self.json_const["windowTitle"]