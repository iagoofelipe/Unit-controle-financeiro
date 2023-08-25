# módulos python
from PySide6.QtCore import QObject, Signal

class Model(QObject):    
    #----------------------------------------------------
    # Signal
    connectionChanged = Signal(bool)
    errorDefined = Signal()

    #----------------------------------------------------
    # property
    @property
    def msgError(self):
        return self._msgError
    
    @property
    def connection(self):
        return self._connection
    
    #----------------------------------------------------
    # setter
    @msgError.setter
    def msgError(self, value: str):
        self._msgError = value
        self.errorDefined.emit()

    
    @connection.setter
    def connection(self, value: bool):
        if value != self._connection:
            self._connection = value
            self.connectionChanged.emit(value)

    #----------------------------------------------------
    def __init__(self):
        super().__init__()
        self._connection = None
        self._msgError = "UNKNOWN_ERROR: Erro desconnhecido"