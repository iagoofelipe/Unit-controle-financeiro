# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Error.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
from . import qrc_rc

class Ui_Error(object):
    def setupUi(self, Error):
        if not Error.objectName():
            Error.setObjectName(u"Error")
        Error.resize(900, 700)
        Error.setMinimumSize(QSize(900, 700))
        self.centralwidget = QWidget(Error)
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
        self.label.setMinimumSize(QSize(100, 100))
        self.label.setMaximumSize(QSize(100, 100))
        self.label.setPixmap(QPixmap(u":/start/img/alerta.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label)


        self.verticalLayout.addWidget(self.widget_3)

        self.msg = QLabel(self.centralwidget)
        self.msg.setObjectName(u"msg")
        font = QFont()
        font.setFamilies([u"Bahnschrift"])
        font.setPointSize(10)
        self.msg.setFont(font)
        self.msg.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.msg)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        Error.setCentralWidget(self.centralwidget)

        self.retranslateUi(Error)

        QMetaObject.connectSlotsByName(Error)
    # setupUi

    def retranslateUi(self, Error):
        Error.setWindowTitle(QCoreApplication.translate("Error", u"MainWindow", None))
        self.label.setText("")
        self.msg.setText(QCoreApplication.translate("Error", u"TYPE_ERROR: descri\u00e7\u00e3o", None))
    # retranslateUi

