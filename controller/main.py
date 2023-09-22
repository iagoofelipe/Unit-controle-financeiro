# módulos python
from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMainWindow

# módulos locais


class CMain(QObject):
    def checkConnection(self):
        self._main_model.connected = self._main_model.db.test_connection()

    @Slot(bool)
    def on_connectionChanged(self, value: bool):
        print("on_connectionChanged:", value)
        if value and self._main_model._uiName == "Iniciar":
            self.mainView.setUi("Login")

        elif value:
            self.mainView.setUi(self._main_model._uiName)

        else:
            self._main_model.errorMessage = "DATABASE_CONNECTION_ERROR: não foi possível conectar-se ao banco de dados"
            self.mainView.setUi("Error")

    def __init__(self, model):
        self._main_model = model
