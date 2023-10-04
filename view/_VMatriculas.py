# módulos python
from PySide6.QtCore import QTimer, QObject
from datetime import datetime as dt

# módulos locais
from Include.src.uis import Ui_Matriculas
# from controller import MatriculasController
# from model import MatriculasModel
# from .app import App

class VMatriculas(QObject, Ui_Matriculas):
    def __init__(self, mainView):
        super(VMatriculas, self).__init__()
        self.setupUi(mainView)

        # self._model = MatriculasModel()
        # self._controller = MatriculasController(self)
        self._main_view = mainView