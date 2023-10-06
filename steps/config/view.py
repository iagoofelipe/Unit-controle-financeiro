# módulos python
from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QTimer, QObject, Slot, Signal
import logging

# módulos locais
from src.uis import Ui_Config
from .controller import ControllerConfig
from .model import ModelConfig

class ViewConfig(QObject, Ui_Config):
    def __init__(self, mainView):
        super(ViewConfig, self).__init__()
        self.setupUi(mainView)
        
        # atributos gerais
        self._main_view = mainView
        self._main_model = mainView._main_model
        self._main_controller = mainView._main_controller

        # atributos privados
        self._timer = QTimer()
        self._model = ModelConfig(self)
        self._controller = ControllerConfig(self)

        # sinais e slots
        self._controller.threadFinished.connect(self.on_threadFinished)
        self._model.saveDefaultsRequired.connect(self._model.on_saveDefaultsRequired)
        
        self.btn_cancelar.clicked.connect(self.btn_cancelar_clicked)
        self.btn_aplicar.clicked.connect(self.btn_aplicar_clicked)
        self.btn_browse.clicked.connect(self.btn_browse_clicked)

        # métodos privados
        self.entry_path_profiles.setText(self._model.path_profiles)
        self.build.setText(self._model.version)
        self.regTable_lengh.setValue(self._model.tabreg_length)
        self.limpar_ao_registrar.setChecked(self._model.clear_entry_values_on_save)

        self.atualizar_auto.setEnabled(False)
        self.timeout.setEnabled(False)
        self.label_10.setEnabled(False)
        self.statusBar.showMessage("As opções de atualizações automáticas não estão disponíveis no momento.")

    @Slot(dict)
    def on_threadFinished(self, values: dict):
        """ thread inicial da interface """

    def btn_cancelar_clicked(self):
        self._main_view.setUiByName("home")

    def btn_aplicar_clicked(self):
        self._model.saveDefaultsRequired.emit()
        self._main_view.setUiByName("home")

    def btn_browse_clicked(self):
        _dir = QFileDialog.getExistingDirectory(
                    dir=self._model.path_profiles,
                    options=QFileDialog.ShowDirsOnly
                )
        
        if _dir != "":
            self.entry_path_profiles.setText(_dir)