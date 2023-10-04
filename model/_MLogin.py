# módulos python
from PySide6.QtCore import QObject

class LoginModel(QObject):
    isAuthenticated = False

    def __init__(self, view):
        super().__init__()
        self._view = view
        self._main_model = self._view._main_model
        self.cfg = self._main_model.cfg_file['LOGIN']

        try:
            self.user = self._main_model.crypto.decode(self.cfg['user'])
            self.password = self._main_model.crypto.decode(self.cfg['password'])
        except:
            self.user = None
            self.password = None