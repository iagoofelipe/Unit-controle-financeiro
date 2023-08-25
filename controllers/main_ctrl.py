# módulos python
from PySide6.QtCore import QObject, Slot, QThreadPool

# módulos locais
from .src.Database.main import Database
from .src.qthread import Worker
from model.model import Model

class MainController(QObject):
    def __init__(self, model: Model):
        super().__init__()
        self._model = model
        self.threadpool = QThreadPool()
        self.db = Database()

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