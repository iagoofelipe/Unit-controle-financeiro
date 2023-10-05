from typing import Literal
from PySide6.QtCore import QTimer, QObject, Slot, Signal
from threading import Thread


class Controller(QObject):
    updateFinished = Signal()
    updateRequired = Signal()

    def __init__(self, view) -> None:
        super().__init__()

        self._view = view
        self._model = view._model
        self._main_controller = view._main_controller

    def on_typeRegistroChanged(self, value):
        self._model.typeRegistro = value
        self.updateRequired.emit()

    @Slot()
    def on_updateRequired(self):
        def function(self):
            self._model.getTabValues()
            self.updateFinished.emit()

        Thread(target=function, args=(self,)).start()



class Model(QObject):
    typeRegistro = "entradas"

    def __init__(self, view) -> None:
        super().__init__()

        self._view = view
        self._main_model = view._main_model
        self.tabreg_length = int(self._main_model.cfg_default['DEFAULT']['tabreg_length'])
    
    def getTabValues(self):
        self._main_model.database.set_table(self.typeRegistro)
        self.tab_values = self._main_model.database.readLastsRowsByIdRange(self.tabreg_length)
        self.tab_values.reverse()
        return self.tab_values
    
    


class Registros(QObject):
    def __init__(self, view) -> None:
        super().__init__()
        
        self._view = view
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        self._model = Model(self)
        self._controller = Controller(self)

        self._view.reg_btn_entrada.clicked.connect(lambda: self._controller.on_typeRegistroChanged("entradas"))
        self._view.reg_btn_saida.clicked.connect(lambda: self._controller.on_typeRegistroChanged("saidas"))
        self._controller.updateRequired.connect(self._controller.on_updateRequired)
        self._controller.updateFinished.connect(self.on_updateFinished)

        self._view.reg_btn_atualizar.clicked.connect(lambda: self._model.updateRequired.emit())
        
        self._view.reg_btn_saida.click()

    @Slot()
    def on_updateFinished(self):
        self._view.setTableWidgetValues(self._view.reg_table, self._model.tab_values, ("ID", "DESCRIÇÃO", "CATEGORIA", "DATA", "PAGAMENTO", "VALOR"))