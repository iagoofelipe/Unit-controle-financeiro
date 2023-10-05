# módulos python
from PySide6.QtCore import QObject, Slot, Signal
from threading import Thread

# módulos locais
from .controller import ControllerRegistros
from .model import ModelRegistros

class ViewRegistros(QObject):
    def __init__(self, view) -> None:
        super().__init__()
        
        self._view = view
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        self._model = ModelRegistros(self)
        self._controller = ControllerRegistros(self)

        self._view.reg_btn_entrada.clicked.connect(lambda: self.on_typeRegistroChanged("entradas"))
        self._view.reg_btn_saida.clicked.connect(lambda: self.on_typeRegistroChanged("saidas"))
        
        self._view.reg_btn_saida.click()

    def on_typeRegistroChanged(self, value):
        self._model.setTypeRegistro(value)
        Thread(target=self.updateValuesThread).start()
        
    def updateValuesThread(self):
        self._model.getTabValues()
        self._view.setTableWidgetValues(self._view.reg_table, self._model.tab_values, ("ID", "DESCRIÇÃO", "CATEGORIA", "DATA", "PAGAMENTO", "VALOR"))