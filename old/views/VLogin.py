from PySide6.QtWidgets import QMainWindow

from .ui import Ui_Login, App

from model import LoginModel
from controllers import LoginController

class LoginView(QMainWindow, Ui_Login, App):
    def __init__(self, master) -> None:
        # métodos de UI
        super(LoginView, self).__init__()
        self.setDefaults(master)

        self._model = LoginModel(self)
        self._controller = LoginController(self)
        self.popup.hide()

        self._model.loginPermission.connect(self.lembrar_senha)
        self.btn_login.clicked.connect(self.btn_loginAction)
        self.login_entry_password.returnPressed.connect(self.btn_loginAction)
        self._model.loginPermission.connect(self._controller.on_loginPermission)

        # caso de login automatico (remember me)
        print("remember de Login:", self._model._remember)
        if self._model._remember:
            self.login_entry_user.setText(self._model.user)
            self.login_entry_password.setText(self._model.password)
            self.login_check_lembrar.setChecked(True)
            self.btn_loginAction()


    def btn_loginAction(self):
        self._model.user = self.login_entry_user.text()
        self._model.password = self.login_entry_password.text()
        self._controller.checkUserPassword()


    def lembrar_senha(self, value):
        se_lembrar = self.login_check_lembrar.isChecked()
        if value:
            if se_lembrar:
                self._model.remember = True
                print("lembrar senha")
            else:
                self._model.remember = False
                print("esquecer senha")


    def showPopup(self):
        self.popup.show()
        self.timer.singleShot(5000, self.popup.hide)
