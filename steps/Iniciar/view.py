# módulos python
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import logging

# módulos locais
from static import WINDOW_TITLE
from src.uis import Ui_Iniciar
from .controller import ControllerIniciar
# model descnecessário

class ViewIniciar(QObject, Ui_Iniciar):
    def __init__(self, mainView):
        super(ViewIniciar, self).__init__()
        
        # atributos gerais
        self._main_view = mainView
        self._main_model = mainView._main_model
        self._main_controller = mainView._main_controller

        # atributos privados
        self._timer = QTimer()
        self._controller = ControllerIniciar(self)
        self._wid = 2

        # métodos privados
        self._main_view.setWindowTitle(WINDOW_TITLE)
        logging.debug("iniciando timer")
        self.setupUi(mainView)
        self._timer.timeout.connect(self.startAnim)
        self._timer.start(1000)

        # sinais e slots
        self._controller.threadFinished.connect(self.on_threadFinished)

    @Slot(dict)
    def on_threadFinished(self, values:dict):
        logging.info("thread INICIAL finalizado")
        
        if values['fail']:
            logging.info(values['error'])
            self._main_model.errorMessage = values['error']
            self._main_view.setUiByName("error")
        else:
            self._main_view.setUiByName("login")

        self._timer.stop()

    def startAnim(self):
        if self._wid == 4:
            self._wid = 1
        
        if self._wid == 1:
            self.__getattribute__(f"circulo3").setStyleSheet(u"background-color: rgb(165, 166, 159)")
        else:
            self.__getattribute__(f"circulo{self._wid-1}").setStyleSheet(u"background-color: rgb(165, 166, 159)")

        self.__getattribute__(f"circulo{self._wid}").setStyleSheet(u"background-color: rgb(119, 120, 115)")
        self._wid += 1


