# módulos python
from PySide6.QtCore import QObject, QTimer, Signal
import logging

# módulos locais

class ModelName(QObject):
    def __init__(self, view):
        super().__init__()

        # atributos gerais
        self._view = view
        self._main_model = view._main_model

        # atributos privados
        self._timer = QTimer()

        # métodos gerais
        # métodos privados

    #-------------------------------------
    # property
    #-------------------------------------
    # Signal
    #-------------------------------------