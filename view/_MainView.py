# módulos python
from PySide6.QtWidgets import QMainWindow
import logging

# módulos locais
from ._VIniciar import VIniciar
from ._VLogin import VLogin
from ._VError import VError
from ._VMatriculas import VMatriculas

class MainView(QMainWindow):
    def __init__(self, main_model, main_controller):
        super(MainView, self).__init__()
        logging.info("MainView inicializando interface iniciar")
        self.setUiByName("Iniciar")
        
        self._main_model = main_model
        self._main_controller = main_controller

        self._main_controller.initFinished.connect(self._main_controller.on_initFinished)
        self._main_controller.initFinished.connect(self.v_initFinished)


    def v_initFinished(self):
        logging.info("MainView inicializando interface login")
        self.setUiByName("Login")

    def setUiByName(self, uiName):
        try:
            match uiName:
                case "Login":
                    VLogin(self)
                case "Iniciar":
                    VIniciar(self)
                case "Error":
                    VError(self)
                case "Matriculas":
                    VMatriculas(self)
                case _:
                    logging.error("MainView.setUiByName UNKNOW UINAME")
                    exit()
        except:
            self._main_model.errorMessage = "LOADING_ERROR: erro inesperado durante a inicialização, feche o programa e tente novamente"
            VError(self)
