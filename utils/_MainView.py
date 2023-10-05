# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer
import logging

# módulos locais
from steps.Iniciar import ViewIniciar
from steps.Login import ViewLogin
from steps.Error import ViewError
from steps.Home import ViewHome

class MainView(QMainWindow):
    def __init__(self, main_model, main_controller):
        super(MainView, self).__init__()
        
        # atributos gerais
        self._main_model = main_model
        self._main_controller = main_controller
        self._timer = QTimer()
        
        # métodos privados
        self.setUiByName("iniciar")
        self.setWindowTitle("Unit - Gestão")
    
    def setUiByName(self, uiName: str):
        uiName = uiName.lower()
        uis = dict(iniciar=ViewIniciar, login=ViewLogin, error=ViewError, home=ViewHome)
        
        logging.debug(f"alterando ui principal para {uiName.upper()}")
        if uiName not in uis:
            logging.debug(f"{uiName.upper()} ui não encontrada!")
            return

        uis[uiName](self)