# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PopUpWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(794, 617)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.Data1PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.Data1PlayButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Data1PlayButton.setObjectName("Data1PlayButton")
        self.verticalLayout_6.addWidget(self.Data1PlayButton)
        self.Data1StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.Data1StopButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Data1StopButton.setObjectName("Data1StopButton")
        self.verticalLayout_6.addWidget(self.Data1StopButton)
        self.horizontalLayout_4.addLayout(self.verticalLayout_6)
        self.Data1TimeWidget = PlotWidget(self.centralwidget)
        self.Data1TimeWidget.setObjectName("Data1TimeWidget")
        self.horizontalLayout_4.addWidget(self.Data1TimeWidget)
        self.Data1FFTWidget = PlotWidget(self.centralwidget)
        self.Data1FFTWidget.setObjectName("Data1FFTWidget")
        self.horizontalLayout_4.addWidget(self.Data1FFTWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Data2PlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.Data2PlayButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Data2PlayButton.setObjectName("Data2PlayButton")
        self.verticalLayout_7.addWidget(self.Data2PlayButton)
        self.Data2StopButton = QtWidgets.QPushButton(self.centralwidget)
        self.Data2StopButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.Data2StopButton.setObjectName("Data2StopButton")
        self.verticalLayout_7.addWidget(self.Data2StopButton)
        self.horizontalLayout_5.addLayout(self.verticalLayout_7)
        self.Data2TimeWidget = PlotWidget(self.centralwidget)
        self.Data2TimeWidget.setObjectName("Data2TimeWidget")
        self.horizontalLayout_5.addWidget(self.Data2TimeWidget)
        self.Data2FFTWidget = PlotWidget(self.centralwidget)
        self.Data2FFTWidget.setObjectName("Data2FFTWidget")
        self.horizontalLayout_5.addWidget(self.Data2FFTWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ComparePlayButton = QtWidgets.QPushButton(self.centralwidget)
        self.ComparePlayButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.ComparePlayButton.setObjectName("ComparePlayButton")
        self.verticalLayout_8.addWidget(self.ComparePlayButton)
        self.CompareStopButton = QtWidgets.QPushButton(self.centralwidget)
        self.CompareStopButton.setMaximumSize(QtCore.QSize(200, 16777215))
        self.CompareStopButton.setObjectName("CompareStopButton")
        self.verticalLayout_8.addWidget(self.CompareStopButton)
        self.horizontalLayout_6.addLayout(self.verticalLayout_8)
        self.CompareTimeWidget = PlotWidget(self.centralwidget)
        self.CompareTimeWidget.setObjectName("CompareTimeWidget")
        self.horizontalLayout_6.addWidget(self.CompareTimeWidget)
        self.CompareFFTWidget = PlotWidget(self.centralwidget)
        self.CompareFFTWidget.setObjectName("CompareFFTWidget")
        self.horizontalLayout_6.addWidget(self.CompareFFTWidget)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Data1PlayButton.setText(_translate("MainWindow", "Play"))
        self.Data1StopButton.setText(_translate("MainWindow", "Stop"))
        self.Data2PlayButton.setText(_translate("MainWindow", "Play"))
        self.Data2StopButton.setText(_translate("MainWindow", "Stop"))
        self.ComparePlayButton.setText(_translate("MainWindow", "Play"))
        self.CompareStopButton.setText(_translate("MainWindow", "Stop"))

from pyqtgraph import PlotWidget
