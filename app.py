# módulos python
from PySide6.QtWidgets import QApplication
import sys

# módulos locais
from model import MainModel
from controller import MainController
from view import MainView


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_model = MainModel() # funções e ações
        self.main_controller = MainController(self.main_model)
        self.main_view = MainView(self.main_model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())