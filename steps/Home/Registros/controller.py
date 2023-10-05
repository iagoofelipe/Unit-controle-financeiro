# módulos python
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread

# módulos locais

class ControllerRegistros(QObject):
    # updateFinished = Signal()
    # updateRequired = Signal()

    def __init__(self, view) -> None:
        super().__init__()

        self._view = view
        self._model = view._model
        self._main_controller = view._main_controller

    # def on_typeRegistroChanged(self, value):
    #     self._model.typeRegistro = value
    #     self.updateRequired.emit()

    # @Slot()
    # def on_updateRequired(self):
    #     def function(self):
    #         self._model.getTabValues()
    #         self.updateFinished.emit()

    #     Thread(target=function, args=(self,)).start()

    def registrar(self):
        pass