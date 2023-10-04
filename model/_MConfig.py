# módulos python
from PySide6.QtCore import QObject
from my_tools import reg_windows
import os

# módulos locais

class ModelConfig(QObject):
    def __init__(self, view):
        super().__init__()
        self._view = view
        self._main_model = self._view._main_model

        try:
            tabreg_length = self._main_model.cfg_file['DEFAULT']['tabreg_length']
        except KeyError:
            tabreg_length = 20
            # self._main_model.updateCfgDefault(DEFAULT={"tabreg_length":20})

        self.tabreg_length:int = int(tabreg_length)
        self.build_version:str = self._main_model.cfg_file['DEFAULT']['version']

        try:
            self.path_profiles = self._main_model.cfg_file['DEFAULT']['path_profiles']
        except KeyError:
            self.path_profiles = os.path.join(reg_windows["USERPROFILE"], "Documents", "Unit")

        if not os.path.exists(self.path_profiles):
            os.mkdir(self.path_profiles)


    def setCfgValues(self):
        values = {
           "tabreg_length": str(self.tabreg_length), 
           "path_profiles": self.path_profiles
        }
        
        self._main_model.cfg_file['DEFAULT'].update(values)
        self._main_model.updateCfgDefault()