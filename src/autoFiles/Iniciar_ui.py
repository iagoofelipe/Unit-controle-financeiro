# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Iniciar.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QMainWindow, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
from . import qrc_rc

class Ui_Iniciar(object):
    def setupUi(self, Iniciar):
        if not Iniciar.objectName():
            Iniciar.setObjectName(u"Iniciar")
        Iniciar.resize(900, 700)
        Iniciar.setMinimumSize(QSize(900, 700))
        self.centralwidget = QWidget(Iniciar)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QSize(230, 109))
        self.label.setMaximumSize(QSize(230, 109))
        self.label.setPixmap(QPixmap(u":/start/img/logo_pedras_vivas_maior.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        self.label_processo = QLabel(self.centralwidget)
        self.label_processo.setObjectName(u"label_processo")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.label_processo.setFont(font)
        self.label_processo.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_processo)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout = QHBoxLayout(self.widget_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widget = QWidget(self.widget_2)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(60, 28))
        self.widget.setMaximumSize(QSize(60, 28))
        self.widget.setStyleSheet(u"border-radius: 5")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.circulo2 = QWidget(self.widget)
        self.circulo2.setObjectName(u"circulo2")
        self.circulo2.setStyleSheet(u"background-color: rgb(165, 166, 159)")

        self.gridLayout.addWidget(self.circulo2, 0, 2, 1, 1)

        self.circulo3 = QWidget(self.widget)
        self.circulo3.setObjectName(u"circulo3")
        self.circulo3.setStyleSheet(u"background-color: rgb(165, 166, 159)")

        self.gridLayout.addWidget(self.circulo3, 0, 3, 1, 1)

        self.circulo1 = QWidget(self.widget)
        self.circulo1.setObjectName(u"circulo1")
        self.circulo1.setStyleSheet(u"background-color: rgb(119, 120, 115);")

        self.gridLayout.addWidget(self.circulo1, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.widget)


        self.verticalLayout.addWidget(self.widget_2)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        Iniciar.setCentralWidget(self.centralwidget)

        self.retranslateUi(Iniciar)

        QMetaObject.connectSlotsByName(Iniciar)
    # setupUi

    def retranslateUi(self, Iniciar):
        Iniciar.setWindowTitle(QCoreApplication.translate("Iniciar", u"MainWindow", None))
        self.label.setText("")
        self.label_processo.setText(QCoreApplication.translate("Iniciar", u"iniciando conex\u00e3o com o servidor", None))
    # retranslateUi

