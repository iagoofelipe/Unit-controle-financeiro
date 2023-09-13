# módulos python
from PySide6.QtCore import QObject, Signal
from my_tools import File, resource_path

# módulos locais
from .main import MMain

class LoginModel(MMain):
    #-----------------------------------------------------------------------------
    # gerais
    loginPermission = Signal(bool)
    
    #-----------------------------------------------------------------------------
    # propriedades
    

    
    @property
    def permission(self):
        return self._permission

    @permission.setter
    def permission(self, value: bool):
        self._permission = value
        self.loginPermission.emit(value)

    #-----------------------------------------------------------------------------
    def __init__(self):
        super(LoginModel, self).__init__()

        self._users = self.getUsers()
        self._permission = False