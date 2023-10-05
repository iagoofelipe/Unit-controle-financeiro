# módulos python
from PySide6.QtWidgets import QApplication, QMainWindow
import sys, logging, os

# módulos locais
from utils import MainModel, MainController, MainView
from static import LOGS

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_model = MainModel()
        self.main_controller = MainController(self.main_model)
        self.main_view = MainView(self.main_model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    if not os.path.exists(LOGS.PATH):
        os.mkdir(LOGS.PATH)

    logging.basicConfig(level=LOGS.LEVEL, filename=LOGS.PATH+"main.log", format="%(asctime)s - %(levelname)s - %(message)s")
    logging.debug("iniciando App")
    app = App(sys.argv)
    sys.exit(app.exec())