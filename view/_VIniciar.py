# módulos python
from PySide6.QtCore import QTimer, QObject
import logging

# módulos locais
from Include.src.uis import Ui_Iniciar

class VIniciar(QObject, Ui_Iniciar):
    start = None
    className = "VIniciar"
    __widNum = 2

    def __init__(self, mainView):
        super(VIniciar, self).__init__()
        self.setupUi(mainView)
        self.timer = QTimer(self)

        self.timer.timeout.connect(self.startAnim)
        self.timer.start(1000)
        logging.info("view.VIniciar inicializado")


    def startAnim(self):
        if self.__widNum == 4:
            self.__widNum = 1
        
        if self.__widNum == 1:
            self.__getattribute__(f"circulo3").setStyleSheet(u"background-color: rgb(165, 166, 159)")
        else:
            self.__getattribute__(f"circulo{self.__widNum-1}").setStyleSheet(u"background-color: rgb(165, 166, 159)")

        self.__getattribute__(f"circulo{self.__widNum}").setStyleSheet(u"background-color: rgb(119, 120, 115)")
        self.__widNum += 1

