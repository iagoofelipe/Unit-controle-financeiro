# módulos python
from PySide6.QtCore import QObject, Slot, QThreadPool

# módulos locais
from .src import Database
from .src.qthread import Worker

class MatriculasController(object):
    # from model.model import Model
    
    # _model = Model
    db = Database()
    
    @Slot(str)
    def on_typeRegistroChanged(self, typeRegistro):
        self.regUpdateValues(typeRegistro)


    def regUpdateValues(self, typeRegistro=None):
        print(typeRegistro)
        if typeRegistro == None:
            typeRegistro = self._model.typeRegistro

        if not self.db.connect():
            self._model.msgError = "DATABASE_CONNECTION_ERROR"
            return

        self.db.set_table(typeRegistro)
        _valuesMeses = self.db.read_column("data")
        valuesTable = self.db.read()
        valuesTable.reverse()

        valuesMeses = []
        for value in _valuesMeses:
            if value[3:] not in valuesMeses:
                valuesMeses.append(value[3:])
        
        valuesMeses.reverse()
        self._model.mesesFilter = valuesMeses
        self._model.regCategorias = self._model.json_const["registros"]["categoria_" + typeRegistro]
        self._model.regTableValues = valuesTable


    @Slot(dict)
    def on_regFormSaved(self, values: dict):
        self.db.connect()
        self.db.set_table(self._model.typeRegistro)
        self.db.create(**values)
        self.db.close()

        # self._model.

    