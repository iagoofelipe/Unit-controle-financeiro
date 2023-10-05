# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import logging

# módulos locais
from static import WINDOW_TITLE
from src.uis import Ui_Login
from .controller import ControllerLogin
from .model import ModelLogin

class ViewLogin(QObject, Ui_Login):
    def __init__(self, mainView):
        super(ViewLogin, self).__init__()
        self.setupUi(mainView)
        
        # atributos gerais
        self._main_view = mainView
        self._main_model = mainView._main_model
        self._main_controller = mainView._main_controller

        # atributos privados
        self._timer = QTimer()
        self._model = ModelLogin(self)
        self._controller = ControllerLogin(self)

        # sinais e slots
        self._controller.threadFinished.connect(self.on_threadFinished)
        self._controller.accessAuthorized.connect(self.on_accessAuthorized)
        self.btn_login.clicked.connect(self.btn_login_cliked)

        # métodos privados
        self.popup.hide()
        self.btn_login.blockSignals(True)
        self._main_view.setWindowTitle(WINDOW_TITLE)

    @Slot()
    def on_threadFinished(self):
        """ thread inicial da interface """
        logging.info("thread LOGIN finished")
        self.btn_login.blockSignals(False)
        
        if self._model.remember:
            self._controller.checkUser()


    def btn_login_cliked(self):
        self._model.user = self.login_entry_user.text()
        self._model.password = self.login_entry_password.text()
        self._model.remember = self.login_check_lembrar.isChecked()
        self._controller.checkUser()

    @Slot(bool)
    def on_accessAuthorized(self, value:bool):
        if value:
            self._main_view.setUiByName("home")
        else:
            self.popup.show()
            self._timer.singleShot(5000, lambda: self.popup.hide())