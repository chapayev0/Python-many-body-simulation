# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'maindgUQpz.ui'
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
        MainWindow.resize(800, 485)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_bar = QFrame(self.centralwidget)
        self.title_bar.setObjectName(u"title_bar")
        self.title_bar.setMinimumSize(QSize(0, 30))
        self.title_bar.setMaximumSize(QSize(16777215, 30))
        self.title_bar.setFrameShape(QFrame.StyledPanel)
        self.title_bar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.title_bar)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, -1, -1)
        self.horizontalSpacer = QSpacerItem(705, 16, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

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
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.frame_3)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setMinimumSize(QSize(50, 50))
        self.home_btn.setMaximumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.home_btn)

        self.set_btn = QPushButton(self.frame_3)
        self.set_btn.setObjectName(u"set_btn")
        self.set_btn.setMinimumSize(QSize(50, 50))

        self.verticalLayout_2.addWidget(self.set_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(100, 0))
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(217, 217, 217);")
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
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.label)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame_7)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.plot_screen = QFrame(self.frame_4)
        self.plot_screen.setObjectName(u"plot_screen")
        self.plot_screen.setFrameShape(QFrame.StyledPanel)
        self.plot_screen.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.plot_screen)


        self.horizontalLayout.addWidget(self.frame_4)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
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
        self.home_btn.setText("")
        self.set_btn.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Plot Settings", None))
    # retranslateUi

