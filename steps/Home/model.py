# módulos python
from PySide6.QtCore import QObject, QTimer, Signal
from typing import Literal
import logging

# módulos locais

class ModelHome(QObject):
    def __init__(self, view):
        super().__init__()

        # atributos gerais
        self._view = view
        self._main_model = view._main_model
        self.cfg_default = self._main_model.cfg_default

        # atributos privados
        self._timer = QTimer()

        # métodos gerais
        # métodos privados

    #-------------------------------------
    # property
    #-------------------------------------
    # Signal
    #-------------------------------------