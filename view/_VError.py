# módulos python
from PySide6.QtCore import QObject

# módulos locais
from Include.src.uis import Ui_Error

class VError(QObject, Ui_Error):
    def __init__(self, mainView):
        super(VError, self).__init__()
        self.setupUi(mainView)
        self._main_model = mainView._main_model

        self.msg.setText(self._main_model.errorMessage)
