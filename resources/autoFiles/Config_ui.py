# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFormLayout, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QSpinBox, QVBoxLayout, QWidget)
from . import qrc_rc

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(465, 402)
        Config.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(Config)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btn_path_executavel = QPushButton(self.groupBox)
        self.btn_path_executavel.setObjectName(u"btn_path_executavel")

        self.gridLayout.addWidget(self.btn_path_executavel, 1, 1, 1, 1)

        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.path_executavel = QLineEdit(self.groupBox)
        self.path_executavel.setObjectName(u"path_executavel")

        self.gridLayout.addWidget(self.path_executavel, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_8)

        self.label_9 = QLabel(self.groupBox_2)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_9)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(106, 0))

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_3)

        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_6)

        self.versao = QLabel(self.groupBox_2)
        self.versao.setObjectName(u"versao")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.versao)

        self.build = QLabel(self.groupBox_2)
        self.build.setObjectName(u"build")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.build)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout_2 = QFormLayout(self.groupBox_3)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.atualizar_auto = QCheckBox(self.groupBox_3)
        self.atualizar_auto.setObjectName(u"atualizar_auto")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.atualizar_auto)

        self.timeout = QSpinBox(self.groupBox_3)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setMinimumSize(QSize(80, 0))
        self.timeout.setReadOnly(False)
        self.timeout.setMinimum(5000)
        self.timeout.setMaximum(999999999)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.timeout)

        self.label_10 = QLabel(self.groupBox_3)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setOpenExternalLinks(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_10)

        self.regTable_lengh = QSpinBox(self.groupBox_3)
        self.regTable_lengh.setObjectName(u"regTable_lengh")
        self.regTable_lengh.setMinimumSize(QSize(80, 0))
        self.regTable_lengh.setMinimum(5)
        self.regTable_lengh.setMaximum(1000)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.regTable_lengh)

        self.label_5 = QLabel(self.groupBox_3)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_5)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btn_cancelar = QPushButton(self.widget)
        self.btn_cancelar.setObjectName(u"btn_cancelar")

        self.horizontalLayout.addWidget(self.btn_cancelar)

        self.btn_aplicar = QPushButton(self.widget)
        self.btn_aplicar.setObjectName(u"btn_aplicar")

        self.horizontalLayout.addWidget(self.btn_aplicar)


        self.verticalLayout.addWidget(self.widget)

        Config.setCentralWidget(self.centralwidget)

        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"MainWindow", None))
        self.groupBox.setTitle(QCoreApplication.translate("Config", u"Pacotes", None))
        self.btn_path_executavel.setText(QCoreApplication.translate("Config", u"Browse...", None))
        self.label.setText(QCoreApplication.translate("Config", u"execut\u00e1vel da aplica\u00e7\u00e3o:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config", u"Descri\u00e7\u00e3o", None))
        self.label_8.setText(QCoreApplication.translate("Config", u"Arquitetura:", None))
        self.label_9.setText(QCoreApplication.translate("Config", u"MVC", None))
        self.label_2.setText(QCoreApplication.translate("Config", u"Linguagem:", None))
        self.label_3.setText(QCoreApplication.translate("Config", u"Python", None))
        self.label_4.setText(QCoreApplication.translate("Config", u"Vers\u00e3o:", None))
        self.label_6.setText(QCoreApplication.translate("Config", u"Build:", None))
        self.versao.setText(QCoreApplication.translate("Config", u"1.0", None))
        self.build.setText(QCoreApplication.translate("Config", u"1.0.1", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Config", u"Opcionais", None))
        self.atualizar_auto.setText(QCoreApplication.translate("Config", u"atualizar dados automaticamente", None))
        self.label_10.setText(QCoreApplication.translate("Config", u"per\u00edodo para atualiza\u00e7\u00e3o de dados (ms)", None))
        self.regTable_lengh.setPrefix("")
        self.label_5.setText(QCoreApplication.translate("Config", u"limite de amostragem para tabela Registros", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Config", u"cancelar", None))
        self.btn_aplicar.setText(QCoreApplication.translate("Config", u"aplicar", None))
    # retranslateUi

