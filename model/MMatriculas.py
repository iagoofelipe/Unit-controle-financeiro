# módulos python
from PySide6.QtCore import QObject, Signal
from my_tools import File, resource_path

# módulos locais
from .main import MMain
# from utils import Database

class MatriculasModel(MMain):
    #-----------------------------------------------------------------------------
    # gerais
    typeRegistroChanged = Signal(str)
    regCategoriasChanged = Signal(list)
    
    #-----------------------------------------------------------------------------
    # propriedades
    @property
    def typeRegistro(self) -> str:
        return self._typeRegistro
    
    @typeRegistro.setter
    def typeRegistro(self, value) -> None:
        self._typeRegistro = value
        self.typeRegistroChanged.emit(value)

    def setTypeRegistro(self, value) -> None:
        self.typeRegistro = value

    @property
    def regCategorias(self) -> list:
        return self._regCategorias
    
    def setRegCategorias(self) -> list:
        values = self.json_const["registros"][f"categoria_{self._typeRegistro}"]
        self._regCategorias = values
        self.regCategoriasChanged.emit(values)

    #-----------------------------------------------------------------------------
    def __init__(self):
        super(MatriculasModel, self).__init__()
        self.db.set_table("saidas")
        print(self.db.lastRowId)
        print(self.db.readLastsColumns(10))
