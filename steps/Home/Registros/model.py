# módulos python
from PySide6.QtCore import QObject, QTimer, Signal
from typing import Literal
import logging

# módulos locais

class ModelRegistros(QObject):
    typeRegistro = "entradas"
    values = None # set by viewRegistros (valores de entrada e saida, para registrar no banco de dados)

    def __init__(self, view) -> None:
        super().__init__()

        self._view = view
        self._main_model = view._main_model
        self.tabreg_length = int(self._main_model.cfg_default['DEFAULT']['tabreg_length'])
        self.clear_entry_values_on_save: bool = self._main_model.cfg_default['DEFAULT']['clear_entry_values_on_save'] == "True"
    
    def getTabValues(self):
        self._main_model.database.set_table(self.typeRegistro)
        self.tab_values = self._main_model.database.readLastsRowsByIdRange(self.tabreg_length)
        self.tab_values.reverse()
        return self.tab_values
    
    def setTypeRegistro(self, value:str):
        self.typeRegistro = value

    def saveDbValues(self):
        """ salvando valores de entrada e saida no banco de dados """
        self._main_model.database.set_table(self.typeRegistro)
        self._main_model.database.create(**self.values)