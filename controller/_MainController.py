# módulos python
from typing import Optional
from PySide6.QtCore import QObject, Slot
from PySide6.QtWidgets import QMainWindow
import logging

# módulos locais


class MainController(QObject):
    @Slot()
    def on_initFinished(self):
        logging.info("intial connection finished")
        print(self._main_model.requests.defaults)

    def __init__(self, main_model):
        super().__init__()
        self._main_model = main_model