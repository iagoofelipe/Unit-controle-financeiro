# extensão de métodos para QMainWindow
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QStandardItemModel, QStandardItem
from PySide6.QtWidgets import QTableWidgetItem, QTableWidget, QComboBox, QListView
from typing import Sequence, Iterable
from my_tools import File, resource_path

class App(object):
    interval = File.getFile(resource_path("model/Files/const.json"))["timeout"]
    start = None

    def setDefaults(self, mainView, **kwargs):
        self.setupUi(mainView)
        for i, content in kwargs.items():
            if i == "setTimer":
                self.setTimer(content)
        
    def setTimer(self, objectName):
        try:
            self._timer: QTimer = self._main_view._ui_timers[objectName]
        except KeyError:
            self._main_view._ui_timers[objectName] = QTimer(self)
            self._timer: QTimer = self._main_view._ui_timers[objectName]
            self._timer.timeout.connect(self.start)
        
        self._timer.start(self.interval)

    def setComboboxValues(self, __obj: QComboBox, __Iterable: Iterable):
        count = 0
        __obj.clear()

        for i in __Iterable:
            __obj.addItem("")
            __obj.setItemText(count, i)

            count += 1

    
    def setTableWidgetValues(self, __obj: QTableWidget, __data: Iterable, __header: Sequence[str], columnSize=144):
        __obj.clear()

        if len(__data) == 0:
            __data = []
            for _ in range(len(__header)):
                __data.append("")

        __obj.setRowCount(len(__data))
        __obj.setColumnCount(len(max(__data, key=len)))

        __obj.setHorizontalHeaderLabels(__header)


        for num_row, row in enumerate(__data):
            for num_column, column in enumerate(row):
                item = QTableWidgetItem(str(column))
                item.setTextAlignment(Qt.AlignCenter)
                __obj.setItem(num_row, num_column, item)

                __obj.setColumnWidth(num_column, columnSize)


    def setListViewValues(self, __obj: QListView, __Iterable: Iterable):
        content = QStandardItemModel()
        __obj.setModel(content)
        
        for i in __Iterable:
            item = QStandardItem(i)
            content.appendRow(item)


    # def changeUi(self, ui):
    #     self.close()
    #     ui.setupUi(self)
    #     ui.show()