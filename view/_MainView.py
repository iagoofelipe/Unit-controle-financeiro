# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
import logging

# módulos locais
from ._VIniciar import VIniciar
from ._VLogin import VLogin
from ._VError import VError
from ._VMatriculas import VMatriculas
from ._VConfig import VConfig

class MainView(QMainWindow):
    def __init__(self, main_model, main_controller):
        super(MainView, self).__init__()
        
        self.timer = QTimer(self)
        self._main_model = main_model
        self._main_controller = main_controller

        self._main_controller.initFinished.connect(self._main_controller.on_initFinished)
        self._main_controller.initFinished.connect(self.v_initFinished)

        logging.info("MainView inicializando interface iniciar")
        self.setUiByName("Iniciar")

    def v_initFinished(self):
        logging.info("MainView inicializando interface login")
        self.setUiByName("Login")

    def setUiByName(self, uiName):
        uis = {
            "Login":VLogin,
            "Iniciar":VIniciar,
            "Error":VError,
            "Matriculas":VMatriculas,
            "Config": VConfig
        }
        
        geometry = self.geometry()
        try:
            uis[uiName](self)
        except Exception as e:
            logging.error(f"MainView.setUiByName {e}")
            self._main_model.errorMessage = f"PROCESS_ERROR: {e}"
            VError(self)
        self.setGeometry(geometry)

    def logout(self):
        self._main_model.logout()
        self.setUiByName("Login")