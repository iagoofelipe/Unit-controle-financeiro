# módulos python
from PySide6.QtCore import QObject, Signal, Slot
from threading import Thread

# módulos locais

class ControllerLogin(QObject):
    threadFinished = Signal()
    accessAuthorized = Signal(bool)

    def __init__(self, view):
        super().__init__()
        
        # atributos gerais
        self._view = view
        self._model = view._model
        
        self._main_model = view._main_model
        self._main_controller = view._main_controller
        
        # inicializando thread
        Thread(target=self.on_thread).start()

    @Slot()
    def on_thread(self):
        """ definindo atributos gerais durante inicialização da classe """
        self._main_model.database.set_table("users")
        self._model.users = self._main_model.database.read()

        self.threadFinished.emit()

    def checkUser(self):
        user = self._model.user
        password = self._model.password

        if user in self._model.users:
            if self._model.users[user]['password'] == password:
                self._main_model.username = self._model.users[user]['username']
                self.accessAuthorized.emit(True)
                return True
        
        self.accessAuthorized.emit(False)
        return False

        # try:
        #     self._model.users[user] = password
        #     self.accessAuthorized.emit(True)
        #     return True
        
        # except KeyError:
        #     self.accessAuthorized.emit(False)
        #     return False