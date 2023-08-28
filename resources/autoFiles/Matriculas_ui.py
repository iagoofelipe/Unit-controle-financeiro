# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Matriculas.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QDoubleSpinBox, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListView, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QTextEdit, QVBoxLayout,
    QWidget)
from . import qrc_rc

class Ui_Matriculas(object):
    def setupUi(self, Matriculas):
        if not Matriculas.objectName():
            Matriculas.setObjectName(u"Matriculas")
        Matriculas.resize(900, 700)
        Matriculas.setMinimumSize(QSize(900, 700))
        Matriculas.setStyleSheet(u"")
        self.actionlembrar = QAction(Matriculas)
        self.actionlembrar.setObjectName(u"actionlembrar")
        self.actionlembrar.setCheckable(True)
        self.actionlembrar.setChecked(False)
        self.actionlembrar.setEnabled(True)
        self.actionversao = QAction(Matriculas)
        self.actionversao.setObjectName(u"actionversao")
        self.menu_sair = QAction(Matriculas)
        self.menu_sair.setObjectName(u"menu_sair")
        self.centralwidget = QWidget(Matriculas)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(1)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.wid_sidebar = QWidget(self.centralwidget)
        self.wid_sidebar.setObjectName(u"wid_sidebar")
        self.wid_sidebar.setMinimumSize(QSize(0, 0))
        self.wid_sidebar.setMaximumSize(QSize(90, 16777215))
        self.wid_sidebar.setStyleSheet(u"background-color: rgb(165, 166, 159); color: \"white\";")
        self.verticalLayout_2 = QVBoxLayout(self.wid_sidebar)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 11, 0, 19)
        self.btn_menu = QPushButton(self.wid_sidebar)
        self.btn_menu.setObjectName(u"btn_menu")
        self.btn_menu.setStyleSheet(u"QPushButton{border: 0}")
        icon = QIcon()
        icon.addFile(u":/matriculas/img/menu_white.png", QSize(), QIcon.Active, QIcon.On)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(26, 23))

        self.verticalLayout_2.addWidget(self.btn_menu)

        self.widget_11 = QWidget(self.wid_sidebar)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setStyleSheet(u"QPushButton{border: 0}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_11)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_config = QPushButton(self.widget_11)
        self.btn_config.setObjectName(u"btn_config")
        icon1 = QIcon()
        icon1.addFile(u":/matriculas/img/engrenagem_white.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_config.setIcon(icon1)
        self.btn_config.setIconSize(QSize(26, 43))
        self.btn_config.setCheckable(False)
        self.btn_config.setChecked(False)

        self.verticalLayout_3.addWidget(self.btn_config)

        self.btn_sair = QPushButton(self.widget_11)
        self.btn_sair.setObjectName(u"btn_sair")
        self.btn_sair.setLayoutDirection(Qt.LeftToRight)
        self.btn_sair.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/matriculas/img/matriculas/sair.png", QSize(), QIcon.Normal, QIcon.On)
        self.btn_sair.setIcon(icon2)
        self.btn_sair.setIconSize(QSize(40, 40))
        self.btn_sair.setFlat(True)

        self.verticalLayout_3.addWidget(self.btn_sair)

        self.spacer1 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.spacer1)


        self.verticalLayout_2.addWidget(self.widget_11)

        self.user_name = QLabel(self.wid_sidebar)
        self.user_name.setObjectName(u"user_name")
        self.user_name.setEnabled(True)
        self.user_name.setMinimumSize(QSize(75, 0))
        font = QFont()
        font.setFamilies([u"Yu Gothic UI Semibold"])
        font.setPointSize(13)
        font.setBold(True)
        self.user_name.setFont(font)
        self.user_name.setFocusPolicy(Qt.NoFocus)
        self.user_name.setAcceptDrops(False)
        self.user_name.setLayoutDirection(Qt.LeftToRight)
        self.user_name.setAutoFillBackground(False)
        self.user_name.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.user_name.setScaledContents(False)
        self.user_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.user_name)

        self.logo = QLabel(self.wid_sidebar)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(84, 0))
        self.logo.setLayoutDirection(Qt.RightToLeft)
        self.logo.setPixmap(QPixmap(u":/login/img/login/logo_pedras_vivas.png"))

        self.verticalLayout_2.addWidget(self.logo)


        self.gridLayout.addWidget(self.wid_sidebar, 0, 0, 2, 1)

        self.wid_principal = QWidget(self.centralwidget)
        self.wid_principal.setObjectName(u"wid_principal")
        self.wid_principal.setMaximumSize(QSize(16777215, 16777215))
        self.wid_principal.setStyleSheet(u"QTextEdit:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.wid_principal)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, -1, -1, 31)
        self.tabWidget = QTabWidget(self.wid_principal)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMaximumSize(QSize(16777215, 16777215))
        self.tabWidget.setStyleSheet(u"")
        self.tab_aluno = QWidget()
        self.tab_aluno.setObjectName(u"tab_aluno")
        self.gridLayout_7 = QGridLayout(self.tab_aluno)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.widget_4 = QWidget(self.tab_aluno)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(400, 16777215))
        self.widget_4.setStyleSheet(u"QLabel {color:\"white \"}")
        self.verticalLayout_17 = QVBoxLayout(self.widget_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.widget_6 = QWidget(self.widget_4)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_18 = QVBoxLayout(self.widget_6)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.widget_26 = QWidget(self.widget_6)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, -1, 0, -1)
        self.entry_matriculas_mes_mensalidade = QComboBox(self.widget_26)
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.addItem("")
        self.entry_matriculas_mes_mensalidade.setObjectName(u"entry_matriculas_mes_mensalidade")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.entry_matriculas_mes_mensalidade.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_mes_mensalidade.setSizePolicy(sizePolicy)
        self.entry_matriculas_mes_mensalidade.setMinimumSize(QSize(83, 0))
        self.entry_matriculas_mes_mensalidade.setMaximumSize(QSize(16777215, 16777215))
        self.entry_matriculas_mes_mensalidade.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_mes_mensalidade.setAutoFillBackground(False)
        self.entry_matriculas_mes_mensalidade.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_mes_mensalidade.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.horizontalLayout_6.addWidget(self.entry_matriculas_mes_mensalidade)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.btn_matriculas_salvar = QPushButton(self.widget_26)
        self.btn_matriculas_salvar.setObjectName(u"btn_matriculas_salvar")
        self.btn_matriculas_salvar.setMinimumSize(QSize(71, 20))
        self.btn_matriculas_salvar.setStyleSheet(u"background-color: rgb(229, 229, 229);")

        self.horizontalLayout_6.addWidget(self.btn_matriculas_salvar)


        self.verticalLayout_18.addWidget(self.widget_26)


        self.verticalLayout_17.addWidget(self.widget_6)

        self.widget_27 = QWidget(self.widget_4)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_19 = QVBoxLayout(self.widget_27)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_data_10 = QLabel(self.widget_27)
        self.label_data_10.setObjectName(u"label_data_10")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(8)
        font1.setBold(True)
        self.label_data_10.setFont(font1)
        self.label_data_10.setStyleSheet(u"background-color: rgb(0, 85, 127);")
        self.label_data_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_data_10)

        self.out_matriculas_pendentes = QListView(self.widget_27)
        self.out_matriculas_pendentes.setObjectName(u"out_matriculas_pendentes")
        self.out_matriculas_pendentes.setMinimumSize(QSize(300, 0))
        self.out_matriculas_pendentes.setStyleSheet(u"QListView {\n"
"	background-colorrgb(212, 213, 205)\n"
"}")

        self.verticalLayout_19.addWidget(self.out_matriculas_pendentes)


        self.verticalLayout_17.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_4)
        self.widget_28.setObjectName(u"widget_28")
        self.widget_28.setMaximumSize(QSize(16777215, 16777215))
        self.widget_28.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_20 = QVBoxLayout(self.widget_28)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_data_13 = QLabel(self.widget_28)
        self.label_data_13.setObjectName(u"label_data_13")
        self.label_data_13.setFont(font1)
        self.label_data_13.setStyleSheet(u"background-color: rgb(134, 0, 0);")
        self.label_data_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_data_13)

        self.out_matriculas_vencidos = QListView(self.widget_28)
        self.out_matriculas_vencidos.setObjectName(u"out_matriculas_vencidos")
        self.out_matriculas_vencidos.setMinimumSize(QSize(300, 0))
        self.out_matriculas_vencidos.setStyleSheet(u"QListView {\n"
"	background-colorrgb(212, 213, 205)\n"
"}")

        self.verticalLayout_20.addWidget(self.out_matriculas_vencidos)


        self.verticalLayout_17.addWidget(self.widget_28)

        self.widget_29 = QWidget(self.widget_4)
        self.widget_29.setObjectName(u"widget_29")
        self.widget_29.setMaximumSize(QSize(16777215, 16777215))
        self.widget_29.setSizeIncrement(QSize(0, 0))
        self.verticalLayout_21 = QVBoxLayout(self.widget_29)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_data_14 = QLabel(self.widget_29)
        self.label_data_14.setObjectName(u"label_data_14")
        self.label_data_14.setFont(font1)
        self.label_data_14.setStyleSheet(u"background-color: rgb(134, 0, 0);")
        self.label_data_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_data_14)

        self.out_matriculas_inadimplentes = QListView(self.widget_29)
        self.out_matriculas_inadimplentes.setObjectName(u"out_matriculas_inadimplentes")
        self.out_matriculas_inadimplentes.setMinimumSize(QSize(300, 0))
        self.out_matriculas_inadimplentes.setStyleSheet(u"QListView {\n"
"	background-colorrgb(212, 213, 205)\n"
"}")

        self.verticalLayout_21.addWidget(self.out_matriculas_inadimplentes)


        self.verticalLayout_17.addWidget(self.widget_29)


        self.gridLayout_7.addWidget(self.widget_4, 0, 4, 1, 1)

        self.frame = QFrame(self.tab_aluno)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.groupBox_dados_alunos = QGroupBox(self.frame)
        self.groupBox_dados_alunos.setObjectName(u"groupBox_dados_alunos")
        self.groupBox_dados_alunos.setMaximumSize(QSize(500, 16777215))
        self.groupBox_dados_alunos.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_dados_alunos.setStyleSheet(u"QGroupBox{color: rgb(104, 104, 104)}\n"
"QLineEdit{background-color:white;border:0}\n"
"QLineEdit:hover{background-color: #e5e5e5}\n"
"")
        self.groupBox_dados_alunos.setFlat(True)
        self.groupBox_dados_alunos.setCheckable(False)
        self.gridLayout_13 = QGridLayout(self.groupBox_dados_alunos)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setVerticalSpacing(13)
        self.label_categoria_36 = QLabel(self.groupBox_dados_alunos)
        self.label_categoria_36.setObjectName(u"label_categoria_36")
        self.label_categoria_36.setMinimumSize(QSize(137, 0))
        font2 = QFont()
        font2.setFamilies([u"Yu Gothic UI"])
        font2.setPointSize(12)
        self.label_categoria_36.setFont(font2)
        self.label_categoria_36.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout_13.addWidget(self.label_categoria_36, 6, 0, 1, 1)

        self.label_categoria_39 = QLabel(self.groupBox_dados_alunos)
        self.label_categoria_39.setObjectName(u"label_categoria_39")
        self.label_categoria_39.setMinimumSize(QSize(137, 0))
        self.label_categoria_39.setFont(font2)
        self.label_categoria_39.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_categoria_39, 4, 0, 1, 1)

        self.entry_matriculas_obs = QTextEdit(self.groupBox_dados_alunos)
        self.entry_matriculas_obs.setObjectName(u"entry_matriculas_obs")
        self.entry_matriculas_obs.setStyleSheet(u"QTextEdit {\n"
"	background-color: \"white\";\n"
"	border: 0\n"
"}\n"
"\n"
"QTextEdit:hover {\n"
"	background-color: #e5e5e5;\n"
"}")

        self.gridLayout_13.addWidget(self.entry_matriculas_obs, 6, 1, 1, 1)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_13.addItem(self.verticalSpacer_8, 7, 1, 1, 1)

        self.label_categoria_31 = QLabel(self.groupBox_dados_alunos)
        self.label_categoria_31.setObjectName(u"label_categoria_31")
        self.label_categoria_31.setMinimumSize(QSize(137, 0))
        self.label_categoria_31.setFont(font2)
        self.label_categoria_31.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_categoria_31, 2, 0, 1, 1)

        self.entry_matriculas_status_matricula = QComboBox(self.groupBox_dados_alunos)
        self.entry_matriculas_status_matricula.addItem("")
        self.entry_matriculas_status_matricula.addItem("")
        self.entry_matriculas_status_matricula.setObjectName(u"entry_matriculas_status_matricula")
        sizePolicy.setHeightForWidth(self.entry_matriculas_status_matricula.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_status_matricula.setSizePolicy(sizePolicy)
        self.entry_matriculas_status_matricula.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_status_matricula.setAutoFillBackground(False)
        self.entry_matriculas_status_matricula.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_status_matricula.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_13.addWidget(self.entry_matriculas_status_matricula, 4, 1, 1, 1)

        self.entry_matriculas_dia_vencimento = QComboBox(self.groupBox_dados_alunos)
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.addItem("")
        self.entry_matriculas_dia_vencimento.setObjectName(u"entry_matriculas_dia_vencimento")
        sizePolicy.setHeightForWidth(self.entry_matriculas_dia_vencimento.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_dia_vencimento.setSizePolicy(sizePolicy)
        self.entry_matriculas_dia_vencimento.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_dia_vencimento.setAutoFillBackground(False)
        self.entry_matriculas_dia_vencimento.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_dia_vencimento.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_13.addWidget(self.entry_matriculas_dia_vencimento, 2, 1, 1, 1)

        self.label_categoria_40 = QLabel(self.groupBox_dados_alunos)
        self.label_categoria_40.setObjectName(u"label_categoria_40")
        self.label_categoria_40.setMinimumSize(QSize(137, 0))
        self.label_categoria_40.setFont(font2)
        self.label_categoria_40.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_13.addWidget(self.label_categoria_40, 5, 0, 1, 1)

        self.entry_matriculas_status_mensalidade = QComboBox(self.groupBox_dados_alunos)
        self.entry_matriculas_status_mensalidade.addItem("")
        self.entry_matriculas_status_mensalidade.addItem("")
        self.entry_matriculas_status_mensalidade.addItem("")
        self.entry_matriculas_status_mensalidade.addItem("")
        self.entry_matriculas_status_mensalidade.setObjectName(u"entry_matriculas_status_mensalidade")
        sizePolicy.setHeightForWidth(self.entry_matriculas_status_mensalidade.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_status_mensalidade.setSizePolicy(sizePolicy)
        self.entry_matriculas_status_mensalidade.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_status_mensalidade.setAutoFillBackground(False)
        self.entry_matriculas_status_mensalidade.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_status_mensalidade.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_13.addWidget(self.entry_matriculas_status_mensalidade, 5, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_dados_alunos, 2, 0, 1, 1)

        self.groupBox_matricula = QGroupBox(self.frame)
        self.groupBox_matricula.setObjectName(u"groupBox_matricula")
        self.groupBox_matricula.setMaximumSize(QSize(500, 16777215))
        self.groupBox_matricula.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_matricula.setStyleSheet(u"QGroupBox{color: rgb(104, 104, 104)}\n"
"QLineEdit{background-color:white;border:0}\n"
"QLineEdit:hover{background-color: #e5e5e5}\n"
"")
        self.groupBox_matricula.setFlat(True)
        self.gridLayout_15 = QGridLayout(self.groupBox_matricula)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setHorizontalSpacing(5)
        self.gridLayout_15.setVerticalSpacing(13)
        self.label_1 = QLabel(self.groupBox_matricula)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setMinimumSize(QSize(0, 0))
        self.label_1.setFont(font2)
        self.label_1.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_1, 2, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_matricula)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(0, 0))
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_15.addWidget(self.label_8, 3, 0, 1, 1)

        self.entry_matriculas_aluno = QComboBox(self.groupBox_matricula)
        self.entry_matriculas_aluno.addItem("")
        self.entry_matriculas_aluno.addItem("")
        self.entry_matriculas_aluno.setObjectName(u"entry_matriculas_aluno")
        sizePolicy.setHeightForWidth(self.entry_matriculas_aluno.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_aluno.setSizePolicy(sizePolicy)
        self.entry_matriculas_aluno.setMinimumSize(QSize(257, 0))
        self.entry_matriculas_aluno.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_aluno.setAutoFillBackground(False)
        self.entry_matriculas_aluno.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_aluno.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_15.addWidget(self.entry_matriculas_aluno, 2, 1, 1, 1)

        self.entry_matriculas_turma = QComboBox(self.groupBox_matricula)
        self.entry_matriculas_turma.setObjectName(u"entry_matriculas_turma")
        sizePolicy.setHeightForWidth(self.entry_matriculas_turma.sizePolicy().hasHeightForWidth())
        self.entry_matriculas_turma.setSizePolicy(sizePolicy)
        self.entry_matriculas_turma.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_turma.setAutoFillBackground(False)
        self.entry_matriculas_turma.setStyleSheet(u"QComboBox {\n"
"	background-color: \"white\";\n"
"	border: 0;\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.entry_matriculas_turma.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_15.addWidget(self.entry_matriculas_turma, 3, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_matricula, 0, 0, 1, 1)

        self.groupBox_dados_responsavel = QGroupBox(self.frame)
        self.groupBox_dados_responsavel.setObjectName(u"groupBox_dados_responsavel")
        self.groupBox_dados_responsavel.setMaximumSize(QSize(500, 16777215))
        self.groupBox_dados_responsavel.setLayoutDirection(Qt.LeftToRight)
        self.groupBox_dados_responsavel.setStyleSheet(u"QGroupBox{color: rgb(104, 104, 104)}\n"
"QLineEdit{background-color:white;border:0}\n"
"QLineEdit:hover{background-color: #e5e5e5}\n"
"")
        self.groupBox_dados_responsavel.setFlat(True)
        self.gridLayout_14 = QGridLayout(self.groupBox_dados_responsavel)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setHorizontalSpacing(5)
        self.gridLayout_14.setVerticalSpacing(13)
        self.label_categoria_27 = QLabel(self.groupBox_dados_responsavel)
        self.label_categoria_27.setObjectName(u"label_categoria_27")
        self.label_categoria_27.setMinimumSize(QSize(137, 0))
        self.label_categoria_27.setFont(font2)
        self.label_categoria_27.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_categoria_27, 2, 0, 1, 1)

        self.entry_matriculas_contato = QLineEdit(self.groupBox_dados_responsavel)
        self.entry_matriculas_contato.setObjectName(u"entry_matriculas_contato")
        self.entry_matriculas_contato.setLayoutDirection(Qt.LeftToRight)
        self.entry_matriculas_contato.setAlignment(Qt.AlignCenter)

        self.gridLayout_14.addWidget(self.entry_matriculas_contato, 2, 1, 1, 1)

        self.label_valor_7 = QLabel(self.groupBox_dados_responsavel)
        self.label_valor_7.setObjectName(u"label_valor_7")
        self.label_valor_7.setMinimumSize(QSize(137, 0))
        self.label_valor_7.setFont(font2)
        self.label_valor_7.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_14.addWidget(self.label_valor_7, 0, 0, 1, 1)

        self.entry_matriculas_responsavel = QLineEdit(self.groupBox_dados_responsavel)
        self.entry_matriculas_responsavel.setObjectName(u"entry_matriculas_responsavel")

        self.gridLayout_14.addWidget(self.entry_matriculas_responsavel, 0, 1, 1, 1)


        self.gridLayout_9.addWidget(self.groupBox_dados_responsavel, 1, 0, 1, 1)


        self.gridLayout_7.addWidget(self.frame, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab_aluno, "")
        self.tab_registros_4 = QWidget()
        self.tab_registros_4.setObjectName(u"tab_registros_4")
        self.gridLayout_11 = QGridLayout(self.tab_registros_4)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.widget_8 = QWidget(self.tab_registros_4)
        self.widget_8.setObjectName(u"widget_8")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.reg_mes_filtro = QComboBox(self.widget_8)
        self.reg_mes_filtro.setObjectName(u"reg_mes_filtro")

        self.verticalLayout_4.addWidget(self.reg_mes_filtro)

        self.reg_table = QTableWidget(self.widget_8)
        self.reg_table.setObjectName(u"reg_table")
        self.reg_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)

        self.verticalLayout_4.addWidget(self.reg_table)


        self.gridLayout_11.addWidget(self.widget_8, 1, 1, 1, 1)

        self.widget_entradas = QWidget(self.tab_registros_4)
        self.widget_entradas.setObjectName(u"widget_entradas")
        self.widget_entradas.setMaximumSize(QSize(530, 16777215))
        self.verticalLayout_8 = QVBoxLayout(self.widget_entradas)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.groupBox = QGroupBox(self.widget_entradas)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setStyleSheet(u"")
        self.gridLayout_8 = QGridLayout(self.groupBox)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setVerticalSpacing(25)
        self.label_valor = QLabel(self.groupBox)
        self.label_valor.setObjectName(u"label_valor")
        self.label_valor.setFont(font2)
        self.label_valor.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_valor, 3, 0, 1, 1)

        self.label_data = QLabel(self.groupBox)
        self.label_data.setObjectName(u"label_data")
        self.label_data.setFont(font2)
        self.label_data.setStyleSheet(u"")
        self.label_data.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_data, 2, 0, 1, 1)

        self.label_categoria = QLabel(self.groupBox)
        self.label_categoria.setObjectName(u"label_categoria")
        self.label_categoria.setFont(font2)
        self.label_categoria.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout_8.addWidget(self.label_categoria, 4, 0, 1, 1)

        self.reg_data = QDateEdit(self.groupBox)
        self.reg_data.setObjectName(u"reg_data")
        self.reg_data.setStyleSheet(u"QDateEdit:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.reg_data.setAlignment(Qt.AlignCenter)
        self.reg_data.setCalendarPopup(True)

        self.gridLayout_8.addWidget(self.reg_data, 2, 1, 1, 1)

        self.reg_valor = QDoubleSpinBox(self.groupBox)
        self.reg_valor.setObjectName(u"reg_valor")
        sizePolicy.setHeightForWidth(self.reg_valor.sizePolicy().hasHeightForWidth())
        self.reg_valor.setSizePolicy(sizePolicy)
        self.reg_valor.setStyleSheet(u"QDoubleSpinBox:hover {\n"
"	background-color: #e5e5e5;\n"
"}")
        self.reg_valor.setAlignment(Qt.AlignCenter)
        self.reg_valor.setDecimals(2)
        self.reg_valor.setMaximum(999999.989999999990687)

        self.gridLayout_8.addWidget(self.reg_valor, 3, 1, 1, 1)

        self.reg_categoria = QComboBox(self.groupBox)
        self.reg_categoria.addItem("")
        self.reg_categoria.addItem("")
        self.reg_categoria.setObjectName(u"reg_categoria")
        sizePolicy.setHeightForWidth(self.reg_categoria.sizePolicy().hasHeightForWidth())
        self.reg_categoria.setSizePolicy(sizePolicy)
        self.reg_categoria.setStyleSheet(u"")
        self.reg_categoria.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)

        self.gridLayout_8.addWidget(self.reg_categoria, 4, 1, 1, 1)

        self.label_descricao = QLabel(self.groupBox)
        self.label_descricao.setObjectName(u"label_descricao")
        self.label_descricao.setFont(font2)
        self.label_descricao.setAlignment(Qt.AlignRight|Qt.AlignTop|Qt.AlignTrailing)

        self.gridLayout_8.addWidget(self.label_descricao, 5, 0, 1, 1)

        self.reg_descricao = QTextEdit(self.groupBox)
        self.reg_descricao.setObjectName(u"reg_descricao")
        self.reg_descricao.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.reg_descricao, 5, 1, 1, 1)

        self.widget_7 = QWidget(self.groupBox)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout = QHBoxLayout(self.widget_7)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.reg_btn_entrada = QRadioButton(self.widget_7)
        self.reg_btn_entrada.setObjectName(u"reg_btn_entrada")

        self.horizontalLayout.addWidget(self.reg_btn_entrada)

        self.reg_btn_saida = QRadioButton(self.widget_7)
        self.reg_btn_saida.setObjectName(u"reg_btn_saida")

        self.horizontalLayout.addWidget(self.reg_btn_saida)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)


        self.gridLayout_8.addWidget(self.widget_7, 0, 1, 1, 1)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_8.addWidget(self.label_3, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.groupBox)

        self.btn = QWidget(self.widget_entradas)
        self.btn.setObjectName(u"btn")
        self.horizontalLayout_3 = QHBoxLayout(self.btn)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.reg_btn_registrar = QPushButton(self.btn)
        self.reg_btn_registrar.setObjectName(u"reg_btn_registrar")
        self.reg_btn_registrar.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.reg_btn_registrar)

        self.reg_btn_limpar = QPushButton(self.btn)
        self.reg_btn_limpar.setObjectName(u"reg_btn_limpar")

        self.horizontalLayout_3.addWidget(self.reg_btn_limpar)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_4)


        self.verticalLayout_8.addWidget(self.btn)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_2)


        self.gridLayout_11.addWidget(self.widget_entradas, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_registros_4, "")

        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.wid_principal, 1, 1, 1, 1)

        Matriculas.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(Matriculas)
        self.statusBar.setObjectName(u"statusBar")
        Matriculas.setStatusBar(self.statusBar)

        self.retranslateUi(Matriculas)

        self.btn_sair.setDefault(False)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Matriculas)
    # setupUi

    def retranslateUi(self, Matriculas):
        Matriculas.setWindowTitle(QCoreApplication.translate("Matriculas", u"MainWindow", None))
        self.actionlembrar.setText(QCoreApplication.translate("Matriculas", u"Lembre de mim", None))
        self.actionversao.setText(QCoreApplication.translate("Matriculas", u"vers\u00e3o", None))
        self.menu_sair.setText(QCoreApplication.translate("Matriculas", u"sair", None))
        self.btn_menu.setText("")
        self.btn_config.setText("")
        self.btn_sair.setText("")
        self.user_name.setText(QCoreApplication.translate("Matriculas", u"USUARIO", None))
        self.logo.setText("")
        self.entry_matriculas_mes_mensalidade.setItemText(0, QCoreApplication.translate("Matriculas", u"07/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(1, QCoreApplication.translate("Matriculas", u"06/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(2, QCoreApplication.translate("Matriculas", u"05/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(3, QCoreApplication.translate("Matriculas", u"04/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(4, QCoreApplication.translate("Matriculas", u"03/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(5, QCoreApplication.translate("Matriculas", u"02/2023", None))
        self.entry_matriculas_mes_mensalidade.setItemText(6, QCoreApplication.translate("Matriculas", u"01/2023", None))

        self.btn_matriculas_salvar.setText(QCoreApplication.translate("Matriculas", u"salvar", None))
#if QT_CONFIG(whatsthis)
        self.label_data_10.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
#if QT_CONFIG(accessibility)
        self.label_data_10.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.label_data_10.setText(QCoreApplication.translate("Matriculas", u"PENDENTES", None))
        self.label_data_13.setText(QCoreApplication.translate("Matriculas", u"VENCIDOS", None))
        self.label_data_14.setText(QCoreApplication.translate("Matriculas", u"INADIMPLENTES", None))
        self.groupBox_dados_alunos.setTitle(QCoreApplication.translate("Matriculas", u"Dados de Matr\u00edcula", None))
        self.label_categoria_36.setText(QCoreApplication.translate("Matriculas", u"observa\u00e7\u00f5es:", None))
        self.label_categoria_39.setText(QCoreApplication.translate("Matriculas", u"status matr\u00edcula:", None))
        self.entry_matriculas_obs.setHtml(QCoreApplication.translate("Matriculas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.entry_matriculas_obs.setPlaceholderText("")
        self.label_categoria_31.setText(QCoreApplication.translate("Matriculas", u"dia de vencimento:", None))
        self.entry_matriculas_status_matricula.setItemText(0, QCoreApplication.translate("Matriculas", u"ATIVO", None))
        self.entry_matriculas_status_matricula.setItemText(1, QCoreApplication.translate("Matriculas", u"INATIVO", None))

        self.entry_matriculas_dia_vencimento.setItemText(0, QCoreApplication.translate("Matriculas", u"1", None))
        self.entry_matriculas_dia_vencimento.setItemText(1, QCoreApplication.translate("Matriculas", u"2", None))
        self.entry_matriculas_dia_vencimento.setItemText(2, QCoreApplication.translate("Matriculas", u"3", None))
        self.entry_matriculas_dia_vencimento.setItemText(3, QCoreApplication.translate("Matriculas", u"4", None))
        self.entry_matriculas_dia_vencimento.setItemText(4, QCoreApplication.translate("Matriculas", u"5", None))
        self.entry_matriculas_dia_vencimento.setItemText(5, QCoreApplication.translate("Matriculas", u"6", None))
        self.entry_matriculas_dia_vencimento.setItemText(6, QCoreApplication.translate("Matriculas", u"7", None))
        self.entry_matriculas_dia_vencimento.setItemText(7, QCoreApplication.translate("Matriculas", u"8", None))
        self.entry_matriculas_dia_vencimento.setItemText(8, QCoreApplication.translate("Matriculas", u"9", None))
        self.entry_matriculas_dia_vencimento.setItemText(9, QCoreApplication.translate("Matriculas", u"10", None))
        self.entry_matriculas_dia_vencimento.setItemText(10, QCoreApplication.translate("Matriculas", u"11", None))
        self.entry_matriculas_dia_vencimento.setItemText(11, QCoreApplication.translate("Matriculas", u"12", None))
        self.entry_matriculas_dia_vencimento.setItemText(12, QCoreApplication.translate("Matriculas", u"13", None))
        self.entry_matriculas_dia_vencimento.setItemText(13, QCoreApplication.translate("Matriculas", u"14", None))
        self.entry_matriculas_dia_vencimento.setItemText(14, QCoreApplication.translate("Matriculas", u"15", None))
        self.entry_matriculas_dia_vencimento.setItemText(15, QCoreApplication.translate("Matriculas", u"16", None))
        self.entry_matriculas_dia_vencimento.setItemText(16, QCoreApplication.translate("Matriculas", u"17", None))
        self.entry_matriculas_dia_vencimento.setItemText(17, QCoreApplication.translate("Matriculas", u"18", None))
        self.entry_matriculas_dia_vencimento.setItemText(18, QCoreApplication.translate("Matriculas", u"19", None))
        self.entry_matriculas_dia_vencimento.setItemText(19, QCoreApplication.translate("Matriculas", u"20", None))
        self.entry_matriculas_dia_vencimento.setItemText(20, QCoreApplication.translate("Matriculas", u"21", None))
        self.entry_matriculas_dia_vencimento.setItemText(21, QCoreApplication.translate("Matriculas", u"22", None))
        self.entry_matriculas_dia_vencimento.setItemText(22, QCoreApplication.translate("Matriculas", u"23", None))
        self.entry_matriculas_dia_vencimento.setItemText(23, QCoreApplication.translate("Matriculas", u"24", None))
        self.entry_matriculas_dia_vencimento.setItemText(24, QCoreApplication.translate("Matriculas", u"25", None))
        self.entry_matriculas_dia_vencimento.setItemText(25, QCoreApplication.translate("Matriculas", u"26", None))
        self.entry_matriculas_dia_vencimento.setItemText(26, QCoreApplication.translate("Matriculas", u"27", None))
        self.entry_matriculas_dia_vencimento.setItemText(27, QCoreApplication.translate("Matriculas", u"28", None))
        self.entry_matriculas_dia_vencimento.setItemText(28, QCoreApplication.translate("Matriculas", u"29", None))
        self.entry_matriculas_dia_vencimento.setItemText(29, QCoreApplication.translate("Matriculas", u"30", None))

        self.label_categoria_40.setText(QCoreApplication.translate("Matriculas", u"status mensalidade:", None))
        self.entry_matriculas_status_mensalidade.setItemText(0, QCoreApplication.translate("Matriculas", u"PAGO", None))
        self.entry_matriculas_status_mensalidade.setItemText(1, QCoreApplication.translate("Matriculas", u"PENDENTE", None))
        self.entry_matriculas_status_mensalidade.setItemText(2, QCoreApplication.translate("Matriculas", u"VENCIDO", None))
        self.entry_matriculas_status_mensalidade.setItemText(3, QCoreApplication.translate("Matriculas", u"INADIMPLENTE", None))

        self.groupBox_matricula.setTitle(QCoreApplication.translate("Matriculas", u"Dados do Aluno", None))
        self.label_1.setText(QCoreApplication.translate("Matriculas", u"aluno:", None))
        self.label_8.setText(QCoreApplication.translate("Matriculas", u"turma:", None))
        self.entry_matriculas_aluno.setItemText(0, QCoreApplication.translate("Matriculas", u"ATIVO", None))
        self.entry_matriculas_aluno.setItemText(1, QCoreApplication.translate("Matriculas", u"INATIVO", None))

        self.groupBox_dados_responsavel.setTitle(QCoreApplication.translate("Matriculas", u"Dados do Respons\u00e1vel", None))
        self.label_categoria_27.setText(QCoreApplication.translate("Matriculas", u"contato:", None))
        self.label_valor_7.setText(QCoreApplication.translate("Matriculas", u"respons\u00e1vel:", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_aluno), QCoreApplication.translate("Matriculas", u"Aluno", None))
        self.groupBox.setTitle("")
        self.label_valor.setText(QCoreApplication.translate("Matriculas", u"Valor R$:", None))
        self.label_data.setText(QCoreApplication.translate("Matriculas", u"Data:", None))
        self.label_categoria.setText(QCoreApplication.translate("Matriculas", u"Categoria:", None))
        self.reg_categoria.setItemText(0, QCoreApplication.translate("Matriculas", u"Grupo Focus", None))
        self.reg_categoria.setItemText(1, QCoreApplication.translate("Matriculas", u"Outros", None))

        self.label_descricao.setText(QCoreApplication.translate("Matriculas", u"Descri\u00e7\u00e3o:", None))
        self.reg_descricao.setHtml(QCoreApplication.translate("Matriculas", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.reg_btn_entrada.setText(QCoreApplication.translate("Matriculas", u"entrada", None))
        self.reg_btn_saida.setText(QCoreApplication.translate("Matriculas", u"sa\u00edda", None))
        self.label_3.setText(QCoreApplication.translate("Matriculas", u"Tipo de Registro:", None))
        self.reg_btn_registrar.setText(QCoreApplication.translate("Matriculas", u"registrar", None))
        self.reg_btn_limpar.setText(QCoreApplication.translate("Matriculas", u"limpar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_registros_4), QCoreApplication.translate("Matriculas", u"Registros", None))
    # retranslateUi

