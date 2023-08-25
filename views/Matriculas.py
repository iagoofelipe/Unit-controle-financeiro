from .ui import Ui_Matriculas
from model.model import Model
from controllers.main_ctrl import MainController

class Matriculas(Ui_Matriculas):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self._model: Model = master._model
        self._main_controller: MainController = master._main_controller


    def start(self):
        self.btn_sair.clicked.connect(lambda: self.master.changeUi(objectName="Login"))
        self.user_name.setText(self._model.user)