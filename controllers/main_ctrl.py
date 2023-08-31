# módulos python
from PySide6.QtCore import QObject, Slot, QThreadPool
from PySide6.QtWidgets import QMainWindow

# módulos locais
from .src import Database
from .src.qthread import Worker

from model.model import Model
from .Matriculas_ctrl import MatriculasController

class MainController(QObject, MatriculasController):
    def __init__(self, model: Model):
        from views.main_view import MainView
        
        super(MainController, self).__init__()
        self._model = model
        self.threadpool = QThreadPool()
        self.db = Database()
        self._view: MainView = None


    @property
    def view(self):
        return self._view


    @view.setter
    def view(self, __obj):
        self._view = __obj


    @Slot()
    def check_connection(self):
        def func():
            test = self.db.test_connection()

            if not test:
                self._model.msgError = "DATABASE_CONNECTION_ERROR: Não foi possível estabelecer a conexão com o banco de dados."

            self._model.connection = test
        self.run_thread(func)
    

    @Slot()
    def checkUserPassword(self):
        users = self._model._users
        m_user = self._model.user
        m_password = self._model.password

        for _, user, password in users:
            if user == m_user and password == m_password:
                self._model.permission = True
                return

        self._model.permission = False


    def run_thread(self, slot, *args, **kwargs):
        worker = Worker(slot, *args, **kwargs)
        self.threadpool.start(worker)

    @Slot(object)
    def on_logout(self, master):
        self._model.user = "USUARIO"
        self._model.password = ""
        self._model.remember = False

        master.changeUi(objectName="Login")


    @Slot()
    def on_errorDefined(self):
        self._view.changeUi(self._view.uis["Error"], "Error")
        self._view._ui.msg.setText(self._model.msgError)


    @Slot(bool)
    def on_loginPermission(self, value):
        print("Login autorizado")

        if value:
            self._view.changeUi(objectName="Matriculas")
        else:            
            self._view._ui.showPopup()

    
    @Slot(bool)
    def on_connectionChanged(self, value):
        objectName = self._view.objectName()

        if objectName == "Carregando" and value:
                self._view._ui.label_processo.setText("êxito na conexão!")
                self._view._ui_atual = dict(objectName="Login")
                self._view.timer.singleShot(2000, lambda: self._view.changeUi(**self._view._ui_atual))

        if objectName != "Carregando" and value:
            self._view._ui_atual = dict(objectName="Login")
            self._view.changeUi(**self._view._ui_atual)


    @Slot(tuple)
    def on_uiChanged(self, args):
        master = args[0]
        ui = args[1]()

        master.close()
        ui.setupUi(ui)
        ui.show()
        ui.setGeometry(master.geometry())