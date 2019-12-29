# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome3.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1120, 660)
        MainWindow.setMinimumSize(QtCore.QSize(1120, 660))
        MainWindow.setMaximumSize(QtCore.QSize(1120, 660))
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(370, 100, 420, 120))

        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)

        self.label.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(25)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(12, -12, 211, 51))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(235, 235, 235))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.Button_Tag = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Tag.setGeometry(QtCore.QRect(190, 220, 240, 310))
        self.Button_Tag.setObjectName('Button_Tag')
        self.Button_Tag.setStyleSheet("QPushButton{border-radius: 30px;background-image: url('./button_img/button_tag')}"
                                      "QPushButton:hover{border-radius: 30px;background-image: url('./button_img/button_tag2')}"
                                      "QPushButton:Pressed{border-radius: 30px;background-image: url('./button_img/button_tag2')}")
        self.Button_Game = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Game.setGeometry(QtCore.QRect(470, 220, 240, 310))
        self.Button_Game.setObjectName('Button_Tag')
        self.Button_Game.setStyleSheet("QPushButton{border-radius: 30px;background-image: url('./button_img/button_game')}"
                                      "QPushButton:hover{border-radius: 30px;background-image: url('./button_img/button_game2')}"
                                      "QPushButton:Pressed{border-radius: 30px;background-image: url('./button_img/button_game2')}")

        self.Button_Top = QtWidgets.QPushButton(self.centralwidget)
        self.Button_Top.setGeometry(QtCore.QRect(750, 220, 240, 310))
        self.Button_Top.setObjectName('Button_Tag')
        self.Button_Top.setStyleSheet("QPushButton{border-radius: 30px;background-image: url('./button_img/button_random')}"
                                      "QPushButton:hover{border-radius: 30px;background-image: url('./button_img/button_random2')}"
                                      "QPushButton:Pressed{border-radius: 30px;background-image: url('./button_img/button_random2')}")





        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        #self.Button_Mini.clicked.connect(MainWindow.hide)
        #self.Button_Close.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        #self.Button_Close.setText(_translate("MainWindow", "PushButton"))
        #self.Button_Tag.setText("Mainwindow","")
        #self.Button_Mini.setText(_translate("MainWindow", "PushButton"))
        self.label.setText(_translate("MainWindow", "选择您需要使用的推荐方法"))
        self.label_2.setText(_translate("MainWindow", "Steam推荐 - welcome"))



        


