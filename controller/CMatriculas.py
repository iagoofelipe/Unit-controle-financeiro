# módulos python
from PySide6.QtCore import QObject, Slot, Signal

# módulos locais

class MatriculasController(QObject):
    logoutSignal = Signal()
    updateTableValues = Signal()

    @Slot(str)
    def on_typeRegistroChanged(self, typeRegistro):
        self._model.setRegCategorias()


    @Slot()
    def logout(self):
        self._model.user = "USUARIO"
        self._model.password = ""
        self._model.remember = False

        self._view._main_view.setUi("Login")
        self.logoutSignal.emit()


    def __init__(self, mainView):
        super(MatriculasController, self).__init__()
        self._model = mainView._model
        self._view = mainView

    