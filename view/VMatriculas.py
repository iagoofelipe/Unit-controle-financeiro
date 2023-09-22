# módulos python
from PySide6.QtCore import QTimer, QObject
from datetime import datetime as dt

# módulos locais
from resources.uis import Ui_Matriculas
from controller import MatriculasController
from model import MatriculasModel
from .app import App

class VMatriculas(QObject, Ui_Matriculas, App):
    def __init__(self, mainView):
        super(VMatriculas, self).__init__()
        self.setupUi(mainView)

        self._model = MatriculasModel()
        self._controller = MatriculasController(self)
        self._main_view = mainView

        # btn action
        self.btn_sair.clicked.connect(self._controller.logout)
        self.btn_config.clicked.connect(lambda: self._main_view.setUi("Config"))
        self.reg_btn_limpar.clicked.connect(self.clearRegContents)        

        self.reg_btn_entrada.clicked.connect(lambda: self._model.setTypeRegistro("entradas"))
        self.reg_btn_saida.clicked.connect(lambda: self._model.setTypeRegistro("saidas"))

        # conexões Model e Controller
        self._model.typeRegistroChanged.connect(self._controller.on_typeRegistroChanged)
        self._model.typeRegistroChanged.connect(lambda _: self.clearRegContents())
        self._model.regCategoriasChanged.connect(self.setRegCategoriasValues)
        
        # defaults
        self.setTimer("VMatriculas")
        self.statusBar.hide()
        self.reg_btn_limpar.click()
        self.reg_btn_entrada.click()
        
    
    # def start(self):
    #     """ funções executadas com timer """
    #     print("VMatriculas")
    
    def setRegCategoriasValues(self, values: list):
        self.setComboboxValues(self.reg_categoria, values)

    def clearRegContents(self):
        self.reg_data.setDate(dt.now())
        self.reg_valor.setValue(0.0)
        self.reg_descricao.clear()