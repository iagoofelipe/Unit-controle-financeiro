# módulos python
from PySide6.QtCore import QTimer, QObject, Slot
import logging

# módulos locais
from Include.src.uis import Ui_Login
from Include.controller import LoginController
from Include.model import LoginModel

class VLogin(QObject, Ui_Login):
    def __init__(self, mainView):
        super(VLogin, self).__init__()
        self.setupUi(mainView)
        self.popup.hide()
        self.timer = QTimer(self)

        self._main_view = mainView
        self._main_controller = self._main_view._main_controller
        self._main_model = self._main_view._main_model

        self._model = LoginModel(self)
        self._controller = LoginController(self)

        self.btn_login.clicked.connect(self._controller.on_btnLoginPressed)
        self._controller.authenticated.connect(self.on_authenticated)

        # caso tenha sido iniciado e default.ini LOGIN.remember True
        if self._model.cfg['remember'] == "True" and self.login_entry_user.text() == "":
            self.login_entry_user.setText(self._model.user)
            self.login_entry_password.setText(self._model.password)
            self.login_check_lembrar.setChecked(True)
            self.btn_login.click()

    @Slot(bool)
    def on_authenticated(self, value: bool):
        if value:
            logging.info("acesso autenticado com sucesso")
            self._main_view.setUiByName("Matriculas")
        else:
            self.popup.show()
            self.timer.singleShot(5000, lambda: self.popup.hide())