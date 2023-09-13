# módulos python
from PySide6.QtCore import QObject, Signal
from my_tools import File, resource_path, encode

# módulos locais
from resources.uis import *
from utils import Database, Crypto

class MMain(QObject):
    #----------------------------------------------------
    # gerais
    uis = dict(Error=Ui_Error, Config=Ui_Config, Iniciar=Ui_Iniciar, Login=Ui_Login, Matriculas=Ui_Matriculas)
    db = Database()
    json_const = File.getFile(resource_path("model/Files/const.json"))
    crypto = Crypto()


    def getUsers(self) -> list:
        try:
            self.db.set_table("users")
            values = self.db.read()
        except:
            values = []
            
        return values
    
    def setJsonConst(self, values: dict):
        File.toFile(resource_path("model/Files/const.json"), values)
    #----------------------------------------------------
    # Signal
    uiChanged = Signal()
    connectionChanged = Signal(bool)

    #----------------------------------------------------
    # propriedades
    @property
    def ui(self):
        return self._ui
    
    @ui.setter
    def ui(self, value: object):
        self._ui = value
        self.uiChanged.emit()

    @property
    def connected(self):
        return self._connected
    
    @connected.setter
    def connected(self, value: bool):
        if value != self._connected:
            self.connectionChanged.emit(value)
            self._connected = value

    @property
    def user(self):
        return self._user

    @user.setter
    def user(self, value: str):
        self._user = encode(value, True)
        self.json_const["login"]["user"] = self._user
        self.setJsonConst(self.json_const)


    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value: str):
        self._password = encode(value)
        self.json_const["login"]["password"] = self.crypto.encode(self._password, "str")
        self.setJsonConst(self.json_const)


    @property
    def remember(self):
        return self._remember
    
    @remember.setter
    def remember(self, value: bool):
        self._remember = value
        self.json_const["login"]["remember"] = self._remember
        self.setJsonConst(self.json_const)

    #----------------------------------------------------
    def __init__(self):
        super().__init__()

        self.mainView = None
        self._connected = None
        self._uiName = None
        self.errorMessage = "TYPE_ERROR: descrição"

        self.crypto.key = self.json_const["key"]
        
        self._user = self.json_const["login"]["user"]
        self._password = self.crypto.decode(self.json_const["login"]["password"])
        self._remember = self.json_const["login"]["remember"]