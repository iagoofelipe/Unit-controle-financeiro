from .ui import Ui_Iniciar
from model.model import Model
from controllers.main import MainController
from PySide6.QtCore import QTimer, QObject

class IniciarView(QObject, Ui_Iniciar):
    def __init__(self, master):
        super(IniciarView, self).__init__()
        from .main import MainView
        
        self.master: MainView = master
        self._model: Model = master._model
        self._main_controller: MainController = master._main_controller
        self.timer = QTimer(self)

        self.__widNum = 2

        self.timer.timeout.connect(self.startAnim)
        self.timer.start(700)

    
    def startAnim(self):
        if self.__widNum == 4:
            self.__widNum = 1

        self.__getattribute__(f"circulo{self.__widNum}").setStyleSheet(u"background-color: rgb(119, 120, 115)")
        
        if self.__widNum == 1:
            self.__getattribute__(f"circulo3").setStyleSheet(u"background-color: rgb(165, 166, 159)")
        else:
            self.__getattribute__(f"circulo{self.__widNum-1}").setStyleSheet(u"background-color: rgb(165, 166, 159)")

        self.__widNum += 1