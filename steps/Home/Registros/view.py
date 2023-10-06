# módulos python
from PySide6.QtCore import QObject, Slot, Signal
from threading import Thread
from datetime import datetime as dt

# módulos locais
from .controller import ControllerRegistros
from .model import ModelRegistros

class ViewRegistros(QObject):
    def __init__(self, view) -> None:
        super().__init__()
        
        # atributos gerais
        self._view = view
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        # atributos privados
        self._model = ModelRegistros(self)
        self._controller = ControllerRegistros(self)

        # métodos privados
        self._view.reg_btn_entrada.clicked.connect(lambda: self.on_typeRegistroChanged("entradas"))
        self._view.reg_btn_saida.clicked.connect(lambda: self.on_typeRegistroChanged("saidas"))
        self._view.reg_btn_registrar.clicked.connect(self.btn_registrar_clicked)
        self._view.reg_btn_limpar.clicked.connect(self.btn_limpar_clicked)
        self._view.reg_btn_atualizar.clicked.connect(self.btn_atualizar_clicked)

        self._view.reg_btn_saida.click()
        self._view.reg_data.setDate(dt.now())

    def on_typeRegistroChanged(self, value):
        self._model.setTypeRegistro(value)
        Thread(target=self.updateValuesThread).start()
        
    def updateValuesThread(self):
        # Thread(target=self.updateValuesThread).start()
        try:
            self._model.getTabValues()
            self._view.setTableWidgetValues(self._view.reg_table, self._model.tab_values, ("ID", "DESCRIÇÃO", "CATEGORIA", "DATA", "PAGAMENTO", "VALOR"))
        except RuntimeError:
            pass

    def btn_registrar_clicked(self):
        data = self._view.reg_data.date().toString("dd/MM/yyyy")
        valor = "R$ " + self._view.reg_valor.text()
        categoria = self._view.reg_categoria.currentText()
        descricao = self._view.reg_descricao.toPlainText()
        
        self._model.values = dict(data=data, valor=valor, categoria=categoria, descricao=descricao)
        self._model.saveDbValues()
        self._view.reg_btn_atualizar.click()

        if self._model.clear_entry_values_on_save:
            self._view.reg_btn_limpar.click()

    def btn_limpar_clicked(self):
        self._view.reg_data.setDate(dt.now())
        self._view.reg_valor.setValue(0)
        self._view.reg_categoria.setCurrentIndex(0)
        self._view.reg_descricao.clear()

    def btn_atualizar_clicked(self):
        Thread(target=self.updateValuesThread).start()