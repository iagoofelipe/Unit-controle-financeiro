# módulos python
from PySide6.QtCore import QObject, Slot, Signal
from my_tools import resource_path, File

# módulos locais
from Include.utils import Crypto

class LoginController(QObject):
    authenticated = Signal(bool)
    rememberActive = Signal()

    @Slot()
    def on_btnLoginPressed(self):
        user = self._view.login_entry_user.text()
        password = self._view.login_entry_password.text()
        remember = self._view.login_check_lembrar.isChecked()

        isAuthenticated = self._server.checkUserPassword(user, password)

        if isAuthenticated and remember:
            self._server.setCfgFile(resource_path("Files\default.ini"), LOGIN={"user": self.crypto.encode(user, 'str'), "password": self.crypto.encode(password, 'str'), "remember": "True"})
        else:
            self._server.setCfgFile(resource_path("Files\default.ini"), LOGIN={"user": "None", "password": "None", "remember": "False"})

        self._model.isAuthenticated = isAuthenticated
        self.authenticated.emit(isAuthenticated)


    def __init__(self, view) -> None:
        super().__init__()

        self._view = view
        self._model = self._view._model

        self._main_controller = self._view._main_controller
        self._main_model = self._view._main_model
        self._server = self._main_controller._server

        self.crypto = Crypto(self._main_model.symmetric_key)