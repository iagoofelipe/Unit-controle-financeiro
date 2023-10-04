# módulos python
from PySide6.QtCore import QTimer, QObject, Slot
from datetime import datetime as dt
from typing import Literal
from threading import Thread

# módulos locais
from Include.src.uis import Ui_Matriculas
from Include.controller import ControllerMatriculas
from Include.model import ModelMatriculas
from ._app import App

class VMatriculas(QObject, Ui_Matriculas, App):
    def __init__(self, mainView):
        super(VMatriculas, self).__init__()
        self.setupUi(mainView)
        self.reg_data.setDate(dt.now())

        self._main_view = mainView
        self._main_model = self._main_view._main_model
        self._model = ModelMatriculas(self)
        self._controller = ControllerMatriculas(self)

        self._controller.typeRegistroChanged.connect(self.on_typeRegistroChanged)
        self._controller.regTabValuesChanged.connect(self.on_regTabValuesChanged)

        self.reg_btn_entrada.clicked.connect(lambda: self._controller.typeRegistroChanged.emit("entradas"))
        self.reg_btn_saida.clicked.connect(lambda: self._controller.typeRegistroChanged.emit("saidas"))
        self.reg_btn_registrar.clicked.connect(self.action_btn_registrar)
        self.reg_btn_limpar.clicked.connect(self.action_btn_limpar)
        self.reg_btn_atualizar.clicked.connect(lambda: self._controller.typeRegistroChanged.emit(self._model.typeRegistro))
        self.btn_sair.clicked.connect(self._main_view.logout)
        self.btn_config.clicked.connect(lambda: self._main_view.setUiByName("Config"))

        self.reg_btn_entrada.click()
        usuario = self._model.user.upper() if self._model.user != None else "USUÁRIO"
        self.user_name.setText(usuario)

    @Slot(str)
    def on_typeRegistroChanged(self, _type: Literal['entradas', 'saidas']):
        self._model.typeRegistro = _type
        def fun(_type):
            self._model.getRegistroValues(_type)
            self._controller.regTabValuesChanged.emit()

        Thread(target=fun, args=(_type, )).start()

    @Slot()
    def on_regTabValuesChanged(self):
        try:
            self.setTableWidgetValues(self.reg_table, self._model.reg_values, ["ID", "DESCRIÇÃO", "CATEGORIA", "DATA", "PAGAMENTO", "VALOR"])
        except RuntimeError: # caso já tenha sido alterada a interface e o item não exista mais
            pass

    def action_btn_registrar(self):
        data = self.reg_data.date().toString("dd/MM/yyyy")
        valor = "R$ " + self.reg_valor.text()
        categoria = self.reg_categoria.currentText()
        descricao = self.reg_descricao.toPlainText()

        self._model.setDbRegValues(dict(data=data, valor=valor, categoria=categoria, descricao=descricao))
        self._controller.typeRegistroChanged.emit(self._model.typeRegistro)
        self.reg_btn_limpar.click()

    def action_btn_limpar(self):
        self.reg_data.setDate(dt.now())
        self.reg_valor.setValue(0.0)
        self.reg_descricao.clear()
        self.reg_categoria.setCurrentIndex(0)