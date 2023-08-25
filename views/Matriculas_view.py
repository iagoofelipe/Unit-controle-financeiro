from .ui import Ui_Matriculas
from model.model import Model
from controllers.main_ctrl import MainController

class Matriculas_view(Ui_Matriculas):
    def __init__(self, master):
        super().__init__()
        self.master = master
        self._model: Model = master._model
        self._main_controller: MainController = master._main_controller


    def start(self):
        self.user_name.setText(self._model.user)
        self.reg_btn_entrada.clicked.connect(lambda: self._model.setTypeRegistro("entradas"))
        self.reg_btn_saida.clicked.connect(lambda: self._model.setTypeRegistro("saidas"))
        self.btn_registrar.clicked.connect(self.btnRegistrarAction)

        self._model.typeRegistroChanged.connect(self._main_controller.on_typeRegistroChanged)
        self._model.mesesFilterChanged.connect(self.setValuesMesesFilter)
        self._model.regCategoriasChanged.connect(self.setValuesCategoria)
        self._model.regTableChanged.connect(self.setRegTableValues)
        self._model.regFormSaved.connect(self._main_controller.on_regFormSaved)

        self.reg_btn_entrada.click()
        self.reg_mes_filtro.currentTextChanged.connect(self.setRegTableValuesFilter)

    def getRegFromValues(self):
        data = self.reg_data.date()
        valor = self.reg_valor.text()
        categoria = self.reg_categoria.currentText()
        descricao = self.reg_descricao.toPlainText()

        return dict(data=data, valor=valor, categoria=categoria, descricao=descricao)
    

    def btnRegistrarAction(self):
        self._model.regFormValues = self.getRegFromValues()


    def setValuesCategoria(self, values: list):
        self.master.setComboboxValues(self.reg_categoria, values)

    def setValuesMesesFilter(self, values: list):
        self.master.setComboboxValues(self.reg_mes_filtro, ["TODOS"] + values)

    
    def setRegTableValuesFilter(self, _filter=None):
        self.setRegTableValues(self._model.regTableValues)

    def setRegTableValues(self, values):
        filtro = self.reg_mes_filtro.currentText()

        if filtro != "TODOS":
            new_values = []
            for value in values:
                data = value[-2]
                if filtro == data[3:]:
                    new_values.append(value)
        else:
            new_values = values

        self.master.setTableWidgetValues(self.reg_table, new_values, self._model.regHeaderTableValues)