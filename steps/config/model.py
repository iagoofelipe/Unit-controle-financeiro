# módulos python
from PySide6.QtCore import QObject, QTimer, Signal, Slot
import logging

# módulos locais

class ModelConfig(QObject):
    saveDefaultsRequired = Signal()

    def __init__(self, view):
        super().__init__()

        # atributos gerais
        self._view = view
        self._main_model = view._main_model

        # atributos privados
        self._timer = QTimer()
        self.cfg_default = self._main_model.cfg_default
        
        self.tabreg_length = int(self.cfg_default['DEFAULT']['tabreg_length'])
        self.path_profiles = self.cfg_default['DEFAULT']['path_profiles']
        self.version = self.cfg_default['DEFAULT']['version']
        self.clear_entry_values_on_save = self.cfg_default['DEFAULT']['clear_entry_values_on_save'] == "True"

        # métodos gerais
        # métodos privados

    @Slot()
    def on_saveDefaultsRequired(self):
        self.path_profiles = self._view.entry_path_profiles.text()
        self.tabreg_length = self._view.regTable_lengh.value()
        self.clear_entry_values_on_save = self._view.limpar_ao_registrar.isChecked()
        self.updateCfgDefaults()

    def updateCfgDefaults(self):
        self._main_model.cfg_default = {
            "DEFAULT":{
                "path_profiles":self.path_profiles,
                "tabreg_length":str(self.tabreg_length),
                "clear_entry_values_on_save": str(self.clear_entry_values_on_save)
                }
            }
    #-------------------------------------
    # property
    #-------------------------------------