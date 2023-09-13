import sys
from PySide6.QtWidgets import QApplication
from model import MMain
from controller import CMain
from view import VMain


class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_model = MMain() # funções e ações
        self.main_controller = CMain(self.main_model)
        self.main_view = VMain(self.main_model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    app = App(sys.argv)
    sys.exit(app.exec())