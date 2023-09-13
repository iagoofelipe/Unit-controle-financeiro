# módulos python
from PySide6.QtCore import QTimer, QObject

# módulos locais
from resources.uis import Ui_Error

class VError(QObject, Ui_Error):
    start = None
    className = "VError"

    def __init__(self, mainView):
        super(VError, self).__init__()
        self.setupUi(mainView)
        self.timer = QTimer(self)
        self._main_model = mainView._main_model

        # self.timer.timeout.connect(lambda: print("timer Error"))
        # self.timer.start(1000)

        self.msg.setText(self._main_model.errorMessage)
