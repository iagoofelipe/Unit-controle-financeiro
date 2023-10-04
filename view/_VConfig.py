# módulos python
from PySide6.QtCore import QObject
from PySide6.QtWidgets import QFileDialog

# módulos locais
from Include.src.uis import Ui_Config
from Include.model import ModelConfig

class VConfig(QObject, Ui_Config):
    def __init__(self, mainView):
        super(VConfig, self).__init__()
        self.setupUi(mainView)

        self._main_view = mainView
        self._main_model = self._main_view._main_model
        self._model = ModelConfig(self)

        self.btn_cancelar.clicked.connect(self.changeUi)
        self.btn_browse.clicked.connect(self.open_dialog)
        self.btn_aplicar.clicked.connect(self.action_btn_aplicar)

        self.timeout.setDisabled(True)
        self.atualizar_auto.setDisabled(True)
        self.statusBar.showMessage("As opções de atualização automática não estão disponíveis para este servidor...")

        self.regTable_lengh.setValue(self._model.tabreg_length)
        self.build.setText(self._model.build_version)
        self.entry_path_profiles.setText(self._model.path_profiles)        

    def open_dialog(self):
        frame = QFileDialog.getExistingDirectory(self._main_view, dir=self._model.path_profiles)
        self._model.path_profiles = frame
        self.entry_path_profiles.setText(self._model.path_profiles)        

    def action_btn_aplicar(self):
        self._model.tabreg_length = self.regTable_lengh.value()
        self._model.setCfgValues()
        self.changeUi()

    def changeUi(self):
        self._main_view.setUiByName("Matriculas")