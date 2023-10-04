# módulos python
from PySide6.QtCore import QObject, Signal, Slot

class ControllerMatriculas(QObject):
    regTabValuesChanged = Signal()
    typeRegistroChanged = Signal(str)

    def __init__(self, view):
        super().__init__()
        self._view = view