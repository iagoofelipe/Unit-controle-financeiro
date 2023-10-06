# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
    QSpinBox, QStatusBar, QVBoxLayout, QWidget)

class Ui_Config(object):
    def setupUi(self, Config):
        if not Config.objectName():
            Config.setObjectName(u"Config")
        Config.resize(506, 403)
        Config.setMinimumSize(QSize(0, 0))
        self.centralwidget = QWidget(Config)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.group_pacotes = QGroupBox(self.centralwidget)
        self.group_pacotes.setObjectName(u"group_pacotes")
        self.gridLayout = QGridLayout(self.group_pacotes)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(self.group_pacotes)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.entry_path_profiles = QLineEdit(self.group_pacotes)
        self.entry_path_profiles.setObjectName(u"entry_path_profiles")
        self.entry_path_profiles.setEchoMode(QLineEdit.Normal)
        self.entry_path_profiles.setReadOnly(True)

        self.gridLayout.addWidget(self.entry_path_profiles, 1, 0, 1, 1)

        self.btn_browse = QPushButton(self.group_pacotes)
        self.btn_browse.setObjectName(u"btn_browse")

        self.gridLayout.addWidget(self.btn_browse, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.group_pacotes)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout = QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_6 = QLabel(self.groupBox_2)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_6)

        self.build = QLabel(self.groupBox_2)
        self.build.setObjectName(u"build")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.build)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.group_opcionais = QGroupBox(self.centralwidget)
        self.group_opcionais.setObjectName(u"group_opcionais")
        self.formLayout_2 = QFormLayout(self.group_opcionais)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.atualizar_auto = QCheckBox(self.group_opcionais)
        self.atualizar_auto.setObjectName(u"atualizar_auto")

        self.formLayout_2.setWidget(0, QFormLayout.SpanningRole, self.atualizar_auto)

        self.timeout = QSpinBox(self.group_opcionais)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setMinimumSize(QSize(80, 0))
        self.timeout.setReadOnly(False)
        self.timeout.setMinimum(5000)
        self.timeout.setMaximum(999999999)

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.timeout)

        self.label_10 = QLabel(self.group_opcionais)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setOpenExternalLinks(False)

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.label_10)

        self.regTable_lengh = QSpinBox(self.group_opcionais)
        self.regTable_lengh.setObjectName(u"regTable_lengh")
        self.regTable_lengh.setMinimumSize(QSize(80, 0))
        self.regTable_lengh.setMinimum(5)
        self.regTable_lengh.setMaximum(1000)

        self.formLayout_2.setWidget(3, QFormLayout.LabelRole, self.regTable_lengh)

        self.label_5 = QLabel(self.group_opcionais)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(3, QFormLayout.FieldRole, self.label_5)

        self.limpar_ao_registrar = QCheckBox(self.group_opcionais)
        self.limpar_ao_registrar.setObjectName(u"limpar_ao_registrar")

        self.formLayout_2.setWidget(4, QFormLayout.SpanningRole, self.limpar_ao_registrar)


        self.verticalLayout.addWidget(self.group_opcionais)

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
        self.statusBar = QStatusBar(Config)
        self.statusBar.setObjectName(u"statusBar")
        Config.setStatusBar(self.statusBar)

        self.retranslateUi(Config)

        QMetaObject.connectSlotsByName(Config)
    # setupUi

    def retranslateUi(self, Config):
        Config.setWindowTitle(QCoreApplication.translate("Config", u"MainWindow", None))
        self.group_pacotes.setTitle(QCoreApplication.translate("Config", u"Pacotes", None))
        self.label.setText(QCoreApplication.translate("Config", u"Pasta de destino para exporta\u00e7\u00f5es (padr\u00e3o):", None))
        self.entry_path_profiles.setText(QCoreApplication.translate("Config", u"aaa", None))
        self.btn_browse.setText(QCoreApplication.translate("Config", u"Browse...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Config", u"Descri\u00e7\u00e3o", None))
        self.label_6.setText(QCoreApplication.translate("Config", u"Build:", None))
        self.build.setText(QCoreApplication.translate("Config", u"-VERSION-", None))
        self.group_opcionais.setTitle(QCoreApplication.translate("Config", u"Opcionais", None))
        self.atualizar_auto.setText(QCoreApplication.translate("Config", u"atualizar dados automaticamente", None))
        self.label_10.setText(QCoreApplication.translate("Config", u"per\u00edodo para atualiza\u00e7\u00e3o de dados (ms)", None))
        self.regTable_lengh.setPrefix("")
        self.label_5.setText(QCoreApplication.translate("Config", u"limite de requisi\u00e7\u00f5es para tabela Registros (diretamente proporicional ao tempo)", None))
        self.limpar_ao_registrar.setText(QCoreApplication.translate("Config", u"limpar dados ap\u00f3s registrar", None))
        self.btn_cancelar.setText(QCoreApplication.translate("Config", u"cancelar", None))
        self.btn_aplicar.setText(QCoreApplication.translate("Config", u"aplicar", None))
    # retranslateUi

