# módulos python
from PySide6.QtWidgets import QApplication, QMainWindow
import sys, logging, os

# módulos locais
from Include.model import MainModel
from Include.controller import MainController
from Include.view import MainView

class App(QApplication):
    def __init__(self, sys_argv):
        super(App, self).__init__(sys_argv)
        self.main_model = MainModel()
        self.main_controller = MainController(self.main_model)
        self.main_view = MainView(self.main_model, self.main_controller)
        self.main_view.show()


if __name__ == '__main__':
    log_file = "logs.log"

    if os.path.exists(log_file):
        os.remove(log_file)
    logging.basicConfig(level=logging.DEBUG, filename=log_file, format="%(asctime)s - %(levelname)s - %(message)s")
    
    app = App(sys.argv)
    sys.exit(app.exec())