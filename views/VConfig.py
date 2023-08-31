from PySide6.QtCore import QObject
from .ui import Ui_Config

class ConfigView(QObject, Ui_Config):
    def __init__(self, master):
        super(ConfigView, self).__init__()
        self.master = master


    def start(self):
        self.btn_cancelar.clicked.connect(self.btnCancelarAction)

    def btnCancelarAction(self):
        self.master.changeUi(objectName="Matriculas")
