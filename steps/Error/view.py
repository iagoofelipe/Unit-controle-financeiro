# módulos python
from PySide6.QtCore import QObject

# módulos locais
from src.uis import Ui_Error
from static import WINDOW_TITLE

class ViewError(QObject, Ui_Error):
    def __init__(self, mainView, errorMessage=None):
        super(ViewError, self).__init__()
        self.setupUi(mainView)
        self._main_view.setWindowTitle(WINDOW_TITLE)

        if errorMessage == None:
            self._main_model = mainView._main_model
            self.msg.setText(self._main_model.errorMessage)
        else:
            self.msg.setText(errorMessage)