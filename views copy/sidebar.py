from PySide6.QtCore import QObject, QPropertyAnimation, QEasingCurve

class Sidebar(QObject):
    def __init__(self, master):
        super().__init__()
        from .Matriculas_view import Matriculas_view
        
        self.master: Matriculas_view = master
        self.animation = QPropertyAnimation(self.master.wid_sidebar, b"maximumWidth")

        self.master.btn_config.clicked.connect(self.showConfig)
        self.master.btn_menu.clicked.connect(self.startAnimation)
        self.hideWidgets()

    def hideWidgets(self):
        self.master.user_name.hide()
        self.master.logo.hide()

    def showWidgets(self):
        self.master.user_name.show()
        self.master.logo.show()


    def showConfig(self):
        self.master.timer.stop()
        self.master.changeUi(objectName="Config")


    def startAnimation(self):
        width = self.master.wid_sidebar.width()

        if width == 84:
            newWidth = 44
            self.master.timer.singleShot(501, self.hideWidgets)
        
        else:
            newWidth = 84 
            self.showWidgets()

        self.animation.setDuration(500)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QEasingCurve.OutBounce)
        self.animation.start()