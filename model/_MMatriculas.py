# módulos python
from PySide6.QtCore import QObject
from typing import Literal

# módulos locais
from Include.utils import Database

class ModelMatriculas(QObject):
    typeRegistro = None

    def __init__(self, view):
        super().__init__()
        self.db = Database()
        self._view = view
        self._main_model = self._view._main_model
        self.user = self._main_model.user

    def getRegistroValues(self, _type:Literal["entradas", "saidas"]="entradas", limit:int=20):
        self.db.set_table(_type)
        self.reg_values = self.db.readLastsRowsByIdRange(limit)
        self.reg_values.reverse()
        return self.reg_values

    def setDbRegValues(self, values: dict):
        self.db.set_table(self.typeRegistro)
        self.db.create(**values)