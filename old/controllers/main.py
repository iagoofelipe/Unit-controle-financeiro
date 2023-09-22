# módulos python
from PySide6.QtCore import QObject, Slot, QThreadPool
from PySide6.QtWidgets import QMainWindow

# módulos locais
from .src import Database
from .src.qthread import Worker

class MainController(QObject):
    def __init__(self, model):
        from model.model import Model
    #     from views.main_view import MainView
        
        # super(MainController, self).__init__()
        self._model: Model = model
        self.threadpool = QThreadPool()
        self.db = Database()
        # self.login = LoginController(self)
    #     self._view: MainView = None


    # @property
    # def view(self):
    #     return self._view


    # @view.setter
    # def view(self, __obj):
    #     self._view = __obj


    @Slot()
    def check_connection(self):
        def func():
            print("verificando conexão")
            test = self.db.test_connection()

            if not test:
                self._model.msgError = "DATABASE_CONNECTION_ERROR: Não foi possível estabelecer a conexão com o banco de dados."

            self._model.connection = test
        self.run_thread(func)
    

    


    def run_thread(self, slot, *args, **kwargs):
        worker = Worker(slot, *args, **kwargs)
        self.threadpool.start(worker)

    # @Slot(object)
    # def on_logout(self, master):
    #     self._model.user = "USUARIO"
    #     self._model.password = ""
    #     self._model.remember = False

    #     master.changeUi(objectName="Login")


    @Slot()
    def on_errorDefined(self):
        self._model.ui = self._view.uis["Error"]()
        self._model.ui.msg.setText(self._model.msgError)




    
    @Slot(bool)
    def on_connectionChanged(self, value):
        # caso conectado
        if value:
            self._model.ui = self._view.lastUi(self._view)
        # objectName = self._view.objectName()

        # if objectName == "Iniciar" and value:
        #         self._view._ui.label_processo.setText("êxito na conexão!")
        #         self._view._ui_atual = dict(objectName="Login")
        #         self._view.timer.singleShot(2000, lambda: self._view.changeUi(**self._view._ui_atual))

        # if objectName != "Iniciar" and value:
        #     self._view._ui_atual = dict(objectName="Login")
        #     self._view.changeUi(**self._view._ui_atual)


    @Slot(object)
    def on_uiChanged(self, __obj:QMainWindow | QObject):
        pass