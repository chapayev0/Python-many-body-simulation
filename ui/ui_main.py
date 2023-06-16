# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainIWUEoN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 642)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 35))
        self.title_bar.setMaximumSize(QSize(16777215, 35))
        self.title_bar.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 6, -1, 6)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.title_lbl = QLabel(self.title_bar)
        self.title_lbl.setObjectName(u"title_lbl")
        font = QFont()
        font.setFamily(u"Poppins Medium")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.title_lbl.setFont(font)

        self.horizontalLayout_3.addWidget(self.title_lbl)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.minimize_btn = QPushButton(self.title_bar)
        self.minimize_btn.setObjectName(u"minimize_btn")
        self.minimize_btn.setMaximumSize(QSize(15, 15))
        self.minimize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	\n"
"	background-color: rgb(38, 222, 129);\n"
"	border-color: rgb(38, 222, 129);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.minimize_btn)

        self.maxmize_btn = QPushButton(self.title_bar)
        self.maxmize_btn.setObjectName(u"maxmize_btn")
        self.maxmize_btn.setMaximumSize(QSize(15, 15))
        self.maxmize_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"	border:1px solid;\n"
"	background-color: rgb(69, 170, 242);\n"
"	border-color: rgb(69, 170, 242);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.maxmize_btn)

        self.close_btn = QPushButton(self.title_bar)
        self.close_btn.setObjectName(u"close_btn")
        self.close_btn.setMaximumSize(QSize(15, 15))
        self.close_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"\n"
"	border:1px solid;\n"
"	background-color: rgb(235, 59, 90);\n"
"	border-color: rgb(235, 59, 90);\n"
"	border-radius:7px;\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.close_btn)


        self.verticalLayout.addWidget(self.title_bar)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(50, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame_3)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(50, 50))
        self.home_btn.setMaximumSize(QSize(50, 50))
        font1 = QFont()
        font1.setFamily(u"Ubuntu")
        font1.setPointSize(9)
        self.home_btn.setFont(font1)
        self.home_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"\n"
"background-color: rgb(171, 108, 130);\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(216, 115, 127);\n"
"	\n"
"	\n"
"	\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.home_btn)

        self.clear_dat = QPushButton(self.frame_3)
        self.clear_dat.setObjectName(u"clear_dat")
        self.clear_dat.setMinimumSize(QSize(50, 50))
        font2 = QFont()
        font2.setFamily(u"Ubuntu")
        self.clear_dat.setFont(font2)
        self.clear_dat.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"\n"
"background-color: rgb(171, 108, 130);\n"
"	\n"
"	\n"
"	\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"\n"
"background-color: rgb(216, 115, 127);\n"
"	\n"
"	\n"
"	\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.clear_dat)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(239, 238, 238);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(200, 0))
        self.frame_5.setMaximumSize(QSize(250, 16777215))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color: rgb(233, 233, 233);\n"
"\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 30))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_8)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 20))
        self.label.setStyleSheet(u"background-color: rgb(252, 187, 109);\n"
"")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_7)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_7)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.legend_chk = QCheckBox(self.frame)
        self.legend_chk.setObjectName(u"legend_chk")
        self.legend_chk.setStyleSheet(u"background:none;")
        self.legend_chk.setChecked(True)

        self.verticalLayout_5.addWidget(self.legend_chk)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_10)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.g_edit = QLineEdit(self.frame_10)
        self.g_edit.setObjectName(u"g_edit")
        self.g_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.g_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.g_edit)


        self.verticalLayout_5.addWidget(self.frame_10)

        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_11)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.dt_edit = QLineEdit(self.frame_11)
        self.dt_edit.setObjectName(u"dt_edit")
        self.dt_edit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.dt_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.dt_edit)


        self.verticalLayout_5.addWidget(self.frame_11)

        self.x_lbl = QLineEdit(self.frame)
        self.x_lbl.setObjectName(u"x_lbl")
        self.x_lbl.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.x_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.x_lbl)

        self.y_lbl = QLineEdit(self.frame)
        self.y_lbl.setObjectName(u"y_lbl")
        self.y_lbl.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.y_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.y_lbl)

        self.z_lbl = QLineEdit(self.frame)
        self.z_lbl.setObjectName(u"z_lbl")
        self.z_lbl.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.z_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.z_lbl)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_6 = QFrame(self.frame_7)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 50))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 20))
        self.label_7.setStyleSheet(u"background-color: rgb(252, 187, 109);\n"
"")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_7)

        self.obj_name = QLineEdit(self.frame_6)
        self.obj_name.setObjectName(u"obj_name")
        self.obj_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.obj_name)

        self.frame_14 = QFrame(self.frame_6)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.frame_14)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_7.addWidget(self.label_4)

        self.pe1 = QLineEdit(self.frame_14)
        self.pe1.setObjectName(u"pe1")

        self.horizontalLayout_7.addWidget(self.pe1)

        self.pe2 = QLineEdit(self.frame_14)
        self.pe2.setObjectName(u"pe2")

        self.horizontalLayout_7.addWidget(self.pe2)

        self.pe3 = QLineEdit(self.frame_14)
        self.pe3.setObjectName(u"pe3")

        self.horizontalLayout_7.addWidget(self.pe3)


        self.verticalLayout_7.addWidget(self.frame_14)

        self.frame_12 = QFrame(self.frame_6)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.frame_12)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_8.addWidget(self.label_5)

        self.ve1 = QLineEdit(self.frame_12)
        self.ve1.setObjectName(u"ve1")

        self.horizontalLayout_8.addWidget(self.ve1)

        self.ve2 = QLineEdit(self.frame_12)
        self.ve2.setObjectName(u"ve2")

        self.horizontalLayout_8.addWidget(self.ve2)

        self.ve3 = QLineEdit(self.frame_12)
        self.ve3.setObjectName(u"ve3")

        self.horizontalLayout_8.addWidget(self.ve3)


        self.verticalLayout_7.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_6)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_13)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_13)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_9.addWidget(self.label_6)

        self.mass_edit = QLineEdit(self.frame_13)
        self.mass_edit.setObjectName(u"mass_edit")

        self.horizontalLayout_9.addWidget(self.mass_edit)


        self.verticalLayout_7.addWidget(self.frame_13)

        self.add_btn = QPushButton(self.frame_6)
        self.add_btn.setObjectName(u"add_btn")
        self.add_btn.setMinimumSize(QSize(0, 20))
        self.add_btn.setStyleSheet(u"QPushButton{\n"
"\n"
"border:none;\n"
"	background-color: rgb(74, 255, 71);}\n"
"")

        self.verticalLayout_7.addWidget(self.add_btn)


        self.verticalLayout_4.addWidget(self.frame_6)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 50))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_9)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.obj_list = QListWidget(self.frame_9)
        self.obj_list.setObjectName(u"obj_list")

        self.verticalLayout_8.addWidget(self.obj_list)

        self.remove_btn = QPushButton(self.frame_9)
        self.remove_btn.setObjectName(u"remove_btn")
        self.remove_btn.setStyleSheet(u"background-color: rgb(255, 15, 79);")

        self.verticalLayout_8.addWidget(self.remove_btn)


        self.verticalLayout_4.addWidget(self.frame_9)


        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.plot_screen = QFrame(self.frame_4)
        self.plot_screen.setObjectName(u"plot_screen")
        self.plot_screen.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.plot_screen.setFrameShape(QFrame.StyledPanel)
        self.plot_screen.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.plot_screen)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.nav_bar = QFrame(self.plot_screen)
        self.nav_bar.setObjectName(u"nav_bar")
        self.nav_bar.setMaximumSize(QSize(16777215, 50))
        self.nav_bar.setFrameShape(QFrame.StyledPanel)
        self.nav_bar.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.nav_bar)

        self.plot_top = QFrame(self.plot_screen)
        self.plot_top.setObjectName(u"plot_top")
        font3 = QFont()
        font3.setPointSize(11)
        self.plot_top.setFont(font3)
        self.plot_top.setFrameShape(QFrame.StyledPanel)
        self.plot_top.setFrameShadow(QFrame.Raised)

        self.verticalLayout_6.addWidget(self.plot_top)


        self.horizontalLayout_2.addWidget(self.plot_screen)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title_lbl.setText(QCoreApplication.translate("MainWindow", u"Many Body Simulator", None))
#if QT_CONFIG(tooltip)
        self.minimize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Minimize", None))
#endif // QT_CONFIG(tooltip)
        self.minimize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.maxmize_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Maximize", None))
#endif // QT_CONFIG(tooltip)
        self.maxmize_btn.setText("")
#if QT_CONFIG(tooltip)
        self.close_btn.setToolTip(QCoreApplication.translate("MainWindow", u"Close", None))
#endif // QT_CONFIG(tooltip)
        self.close_btn.setText("")
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.clear_dat.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plot Settings", None))
        self.legend_chk.setText(QCoreApplication.translate("MainWindow", u"Legend", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"G =", None))
        self.g_edit.setText(QCoreApplication.translate("MainWindow", u"39.478", None))
        self.g_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gravitatonal Constnt(G)", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"dt =", None))
        self.dt_edit.setText(QCoreApplication.translate("MainWindow", u"0.001", None))
        self.dt_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Time Step(dt)", None))
        self.x_lbl.setText(QCoreApplication.translate("MainWindow", u"X Position", None))
        self.x_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"X Label", None))
        self.y_lbl.setText(QCoreApplication.translate("MainWindow", u"Y Position", None))
        self.y_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Y Label", None))
        self.z_lbl.setText(QCoreApplication.translate("MainWindow", u"Z Position", None))
        self.z_lbl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Z Label", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Object data", None))
        self.obj_name.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Object Name", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"positions", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"velocities", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"masses", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        self.remove_btn.setText(QCoreApplication.translate("MainWindow", u"Remove", None))
    # retranslateUi

