# módulos python
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import QTimer, Slot, QBasicTimer

# módulos locais
from controller import CMain
from model import MMain
from .VIniciar import VIniciar
from .VError import VError
from .VMatriculas import VMatriculas
from .VLogin import VLogin
from .VConfig import VConfig
from utils import Timer

class VMain(QMainWindow):
    def __init__(self, model, controller):
        super().__init__()
        
        self._main_model: MMain = model
        self._main_controller: CMain = controller
        self._main_timer = QTimer(self)
        self._main_model.mainView = self
        self._main_controller.mainView = self
        # self._child_timer = Timer(self)
        self._child_timer = QBasicTimer()
        self._ui_timers = dict()

        self._main_model.connectionChanged.connect(self._main_controller.on_connectionChanged)

        self._main_timer.timeout.connect(self._main_controller.checkConnection)
        # self._main_timer.timeout.connect(lambda: print("main timer"))
        self._main_timer.start(2000)

        self._main_model.uiChanged.connect(self.on_uiChanged)

        self.setUi("Iniciar")


    def setUi(self, uiName: str | object):
        setUiName = True
        uis = dict(Iniciar=VIniciar, Login=VLogin, Matriculas=VMatriculas, Config=VConfig, Error=VError)
        self.setObjectName("")
        geometry = self.geometry()
        
        for _, timer in self._ui_timers.items():
            timer.stop()

        if uiName in uis:
            self._main_model.ui = uis[uiName](self)
            
        else:
            self._main_model.ui = uiName(self)
        
        if uiName == "Error":
            setUiName = False        

        self.setWindowTitle("Unit - Controle Financeiro")
        self.setGeometry(geometry)
        if setUiName:
            self._main_model._uiName = self.objectName()


    def makeUi(self, ui):
        """ retorna QObject da UI informada """
        class Ui(ui):
            def __init__(self, mainView):
                super(Ui, self).__init__()
                self.setupUi(mainView)
                self.start = None

        return Ui

    
    @Slot()
    def on_uiChanged(self):
        ui = self._main_model.ui

        if ui.start != None:
            ui.start()