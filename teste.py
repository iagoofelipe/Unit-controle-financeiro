# import sys
# from PySide6.QtWidgets import QApplication, QMainWindow
# from resources.uis import Ui_Iniciar

# class VMain(QMainWindow, Ui_Iniciar):
#     def __init__(self):
#         super(VMain, self).__init__()
#         self.setupUi(self)



# class App(QApplication):
#     def __init__(self, sys_argv):
#         super(App, self).__init__(sys_argv)

#         self.main_view = VMain()
#         self.main_view.show()


# if __name__ == '__main__':
#     app = App(sys.argv)
#     sys.exit(app.exec())

class Teste:
    def __init__(self) -> None:
        pass

    @property
    def json(self):
        return self._json

    @json.setter
    def json(self, value):
        print("atraves de setter", value)
        self._json = value


teste = Teste()
teste.json = {"a": 1}
teste.json["a"] = 2
teste.json = {"b": 3}