from .ui import Ui_Login
from model.model import Model
from controllers.main_ctrl import MainController

class Login(Ui_Login):
    def __init__(self, master) -> None:
        # métodos de UI
        super(Login, self).__init__()
        self.master = master
        self._model: Model = master._model
        self._main_controller: MainController = master._main_controller
        
        self._model.loginPermission.connect(self.lembrar_senha)


    def start(self):
        self.popup.hide()
        self.btn_login.clicked.connect(self.btn_loginAction)
        self.login_entry_password.returnPressed.connect(self.btn_loginAction)

        # caso de login automatico (remember me)
        if self._model._remember:
            self.login_entry_user.setText(self._model.user)
            self.login_entry_password.setText(self._model.password)
            self.login_check_lembrar.setChecked(True)
            self.btn_loginAction()


    def btn_loginAction(self):
        self._model.user = self.login_entry_user.text()
        self._model.password = self.login_entry_password.text()
        self._main_controller.checkUserPassword()


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
        self.master.timer.singleShot(5000, self.popup.hide)
