# módulos python
from PySide6.QtCore import QObject, Signal, QDate
from my_tools import encode, File, resource_path
import time

# módulos locais
from controllers.src.Database.main import Database

class MatriculasModel(object):
    regHeaderTableValues = ["id", "descrição", "categoria", "data", "valor"]

    #-------------------------------------------------------------
    # typeRegistro
    typeRegistroChanged = Signal(str)

    @property
    def typeRegistro(self):
        return self._typeRegistro
    
    @typeRegistro.setter
    def typeRegistro(self, value: str):
        self.table = value
        self._typeRegistro = value
        self.typeRegistroChanged.emit(value)

    def setTypeRegistro(self, value: str):
        self.typeRegistro = value
    #-------------------------------------------------------------
    # mesesFilter
    mesesFilterChanged = Signal(list)

    @property
    def mesesFilter(self):
        return self._mesesFilter

    @mesesFilter.setter
    def mesesFilter(self, values: list):
        self._mesesFilter = values
        self.mesesFilterChanged.emit(values)
    #-------------------------------------------------------------
    # regCategorias
    regCategoriasChanged = Signal(list)

    @property
    def regCategorias(self):
        return self._regCategorias
    
    @regCategorias.setter
    def regCategorias(self, values: list):
        self._regCategorias = values
        self.regCategoriasChanged.emit(values)
    #-------------------------------------------------------------
    # regTableValues
    regTableChanged = Signal(list)

    @property
    def regTableValues(self):
        return self._regTableValues

    @regTableValues.setter
    def regTableValues(self, values: list):
        self._regTableValues = values
        self.regTableChanged.emit(values)
    #-------------------------------------------------------------
    # regForm
    regFormSaved = Signal(dict)

    @property
    def regFormValues(self):
        return self._regFormValues
    
    @regFormValues.setter
    def regFormValues(self, values: dict):
        self._regFormValues = values
        
        if "data" in values:
            data = values["data"]
            if type(data) == QDate:
                values["data"] = f"{str(data.day()).rjust(2,'0')}/{str(data.month()).rjust(2,'0')}/{data.year()}"

        self.regFormSaved.emit(values)