from .ui import *
from PySide6.QtWidgets import QMainWindow

class Login(Ui_Login):
    def __init__(self) -> None:
        # métodos de UI
        super(Login, self).__init__()

        # self.popup.hide()

        # self.btn_login.clicked.connect(self.slot_login)
        # self.login_entry_password.returnPressed.connect(self.slot_login)
