# módulos python
from PySide6.QtCore import QObject, Slot

# módulos python

class LoginController(QObject):
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

    @Slot(bool)
    def on_loginPermission(self, value):
        if value:
            self._view._main_view.setUi("Matriculas")
            print("Login autorizado")
        else:            
            self._view.showPopup()

    def __init__(self, mainView):
        super(LoginController, self).__init__()
        self._model = mainView._model
        self._view = mainView

