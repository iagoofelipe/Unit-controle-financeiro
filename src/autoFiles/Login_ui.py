# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import qrc_rc

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        # Login.resize(900, 700)
        Login.setMinimumSize(QSize(900, 700))
        Login.setStyleSheet(u"")
        self.actionlembrar = QAction(Login)
        self.actionlembrar.setObjectName(u"actionlembrar")
        self.actionlembrar.setCheckable(True)
        self.actionlembrar.setChecked(False)
        self.actionlembrar.setEnabled(True)
        self.actionversao = QAction(Login)
        self.actionversao.setObjectName(u"actionversao")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: #E6E6E6")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.login = QWidget(self.centralwidget)
        self.login.setObjectName(u"login")
        self.verticalLayout_2 = QVBoxLayout(self.login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        self.widget_4 = QWidget(self.login)
        self.widget_4.setObjectName(u"widget_4")
        self.gridLayout_4 = QGridLayout(self.widget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.popup = QWidget(self.widget_4)
        self.popup.setObjectName(u"popup")
        self.popup.setMaximumSize(QSize(315, 32))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setBold(True)
        self.popup.setFont(font)
        self.popup.setStyleSheet(u"background-color: rgb(133, 148, 133);\n"
"border-radius: 10px")
        self.horizontalLayout_2 = QHBoxLayout(self.popup)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit = QLineEdit(self.popup)
        self.lineEdit.setObjectName(u"lineEdit")
        font1 = QFont()
        font1.setFamilies([u"Yu Gothic UI Semibold"])
        font1.setPointSize(11)
        font1.setBold(True)
        self.lineEdit.setFont(font1)
        self.lineEdit.setStyleSheet(u"color: white;")
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.lineEdit)


        self.gridLayout_4.addWidget(self.popup, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget_4)

        self.widget = QWidget(self.login)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 315))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.container_login = QWidget(self.widget)
        self.container_login.setObjectName(u"container_login")
        self.container_login.setMaximumSize(QSize(315, 337))
        self.container_login.setFont(font)
        self.container_login.setCursor(QCursor(Qt.ArrowCursor))
        self.container_login.setStyleSheet(u"QWidget {\n"
"	background-color: rgba(63, 66, 49, 100);\n"
"	border-radius: 25px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	background-color: rgb(199, 199, 199);\n"
"}\n"
"\n"
"QLineEdit::hover {\n"
"	\n"
"	background-color: rgb(230, 230, 230);\n"
"}")
        self.icon_user = QLabel(self.container_login)
        self.icon_user.setObjectName(u"icon_user")
        self.icon_user.setGeometry(QRect(40, 60, 40, 40))
        self.icon_user.setStyleSheet(u"")
        self.icon_user.setPixmap(QPixmap(u":/login/img/login/user.png"))
        self.icon_padlock = QLabel(self.container_login)
        self.icon_padlock.setObjectName(u"icon_padlock")
        self.icon_padlock.setGeometry(QRect(40, 130, 40, 40))
        self.icon_padlock.setStyleSheet(u"")
        self.icon_padlock.setPixmap(QPixmap(u":/login/img/login/padlock.png"))
        self.login_entry_password = QLineEdit(self.container_login)
        self.login_entry_password.setObjectName(u"login_entry_password")
        self.login_entry_password.setGeometry(QRect(80, 130, 191, 41))
        self.login_entry_password.setCursor(QCursor(Qt.IBeamCursor))
        self.login_entry_password.setMaxLength(15)
        self.login_entry_password.setFrame(True)
        self.login_entry_password.setEchoMode(QLineEdit.Password)
        self.login_entry_password.setCursorPosition(0)
        self.login_entry_password.setAlignment(Qt.AlignCenter)
        self.login_entry_password.setDragEnabled(False)
        self.login_entry_password.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.login_entry_password.setClearButtonEnabled(False)
        self.login_entry_user = QLineEdit(self.container_login)
        self.login_entry_user.setObjectName(u"login_entry_user")
        self.login_entry_user.setGeometry(QRect(80, 60, 191, 41))
        self.login_entry_user.setCursor(QCursor(Qt.IBeamCursor))
        self.login_entry_user.setInputMethodHints(Qt.ImhNone)
        self.login_entry_user.setMaxLength(15)
        self.login_entry_user.setFrame(True)
        self.login_entry_user.setEchoMode(QLineEdit.Normal)
        self.login_entry_user.setCursorPosition(0)
        self.login_entry_user.setAlignment(Qt.AlignCenter)
        self.login_entry_user.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.login_check_lembrar = QCheckBox(self.container_login)
        self.login_check_lembrar.setObjectName(u"login_check_lembrar")
        self.login_check_lembrar.setGeometry(QRect(100, 200, 111, 17))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI Semibold"])
        font2.setPointSize(9)
        font2.setBold(True)
        self.login_check_lembrar.setFont(font2)
        self.login_check_lembrar.setCursor(QCursor(Qt.ArrowCursor))
        self.login_check_lembrar.setStyleSheet(u"QCheckBox {\n"
"	color: white;\n"
"	background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
"QCheckBox::hover {\n"
"	\n"
"	color: rgb(227, 227, 227);\n"
"}")
        self.btn_login = QPushButton(self.container_login)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(50, 260, 211, 31))
        self.btn_login.setFont(font)
        self.btn_login.setStyleSheet(u"QPushButton {\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	background-color: rgb(110, 125, 111);\n"
"}\n"
"\n"
"QPushButton::hover {\n"
"	\n"
"	background-color: rgb(142, 161, 143);\n"
"}")

        self.gridLayout_3.addWidget(self.container_login, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.verticalLayout.addWidget(self.login)

        self.logos = QWidget(self.centralwidget)
        self.logos.setObjectName(u"logos")
        self.logos.setMaximumSize(QSize(16777215, 113))
        self.horizontalLayout = QHBoxLayout(self.logos)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logo_escola = QFrame(self.logos)
        self.logo_escola.setObjectName(u"logo_escola")
        self.logo_escola.setMinimumSize(QSize(94, 0))
        self.logo_escola.setStyleSheet(u"border-radius: 47px;")
        self.logo_escola.setFrameShape(QFrame.StyledPanel)
        self.logo_escola.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.logo_escola)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.png_logo = QLabel(self.logo_escola)
        self.png_logo.setObjectName(u"png_logo")
        self.png_logo.setStyleSheet(u"")
        self.png_logo.setPixmap(QPixmap(u":/login/img/login/logo_pedras_vivas.png"))

        self.verticalLayout_3.addWidget(self.png_logo)


        self.horizontalLayout.addWidget(self.logo_escola)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.widget_3 = QWidget(self.logos)
        self.widget_3.setObjectName(u"widget_3")
        self.gridLayout_2 = QGridLayout(self.widget_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.widget_2 = QWidget(self.widget_3)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(96, 0))
        self.widget_2.setMaximumSize(QSize(0, 50))
        self.widget_2.setStyleSheet(u"background-color: rgb(110, 125, 111);\n"
"border-radius: 10px;\n"
"")
        self.gridLayout = QGridLayout(self.widget_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logo_unit = QLabel(self.widget_2)
        self.logo_unit.setObjectName(u"logo_unit")
        self.logo_unit.setMinimumSize(QSize(0, 0))
        self.logo_unit.setPixmap(QPixmap(u":/login/img/login/logo_unit.png"))

        self.gridLayout.addWidget(self.logo_unit, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.widget_2, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget_3)


        self.verticalLayout.addWidget(self.logos)

        Login.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.lineEdit, self.login_entry_user)
        QWidget.setTabOrder(self.login_entry_user, self.login_entry_password)
        QWidget.setTabOrder(self.login_entry_password, self.login_check_lembrar)
        QWidget.setTabOrder(self.login_check_lembrar, self.btn_login)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.actionlembrar.setText(QCoreApplication.translate("Login", u"Lembre de mim", None))
        self.actionversao.setText(QCoreApplication.translate("Login", u"vers\u00e3o", None))
        self.lineEdit.setText(QCoreApplication.translate("Login", u"usu\u00e1rio ou senha incorreta!", None))
        self.icon_user.setText("")
        self.icon_padlock.setText("")
        self.login_entry_password.setText("")
        self.login_entry_password.setPlaceholderText(QCoreApplication.translate("Login", u"senha", None))
        self.login_entry_user.setText("")
        self.login_entry_user.setPlaceholderText(QCoreApplication.translate("Login", u"usu\u00e1rio", None))
        self.login_check_lembrar.setText(QCoreApplication.translate("Login", u"lembrar de mim", None))
        self.btn_login.setText(QCoreApplication.translate("Login", u"LOGIN", None))
        self.png_logo.setText("")
        self.logo_unit.setText("")
    # retranslateUi

