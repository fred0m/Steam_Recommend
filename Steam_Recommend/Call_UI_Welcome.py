import sys
import os
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_Welcome import Ui_MainWindow




class Welcome( QMainWindow , Ui_MainWindow):
    def __init__(self,parent = None):
        super(Welcome,self).__init__(parent)
        self.setupUi(self)

        Button_Close = QPushButton(self)
        Button_Close.setObjectName('Button_Close')
        Button_Close.setGeometry(QtCore.QRect(1092, 10, 19, 19))
        style = '''
                            #Button_Close{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_CLOSE1');
                                }
                            #Button_Close:hover{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_CLOSE2');
                                }
                            #Button_Close:Pressed{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_CLOSE2');
                                }
                        '''
        Button_Close.setStyleSheet(style)
        Button_Close.clicked.connect(self.close)

        Button_Mini = QPushButton(self)
        Button_Mini.setObjectName('Button_Mini')
        Button_Mini.setGeometry(QtCore.QRect(1067, 10, 19, 19))
        style = '''
                            #Button_Mini{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_MINI1');
                                }
                            #Button_Mini:hover{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_MINI2');
                                }
                            #Button_Mini:Pressed{
                                border-radius: 30px;
                                background-image: url('./button_img/ICO_MINI2');
                                }
                        '''
        Button_Mini.setStyleSheet(style)
        self.Button_Tag.clicked.connect(lambda: self.Open_Main_Tags())
        self.Button_Game.clicked.connect(lambda: self.Open_Main_Choose_Game())
        self.Button_Top.clicked.connect(lambda: self.Open_Main_Top())




    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None
    def Open_Main_Tags(self):
        os.system("Call_UI_Tags.py")

    def Open_Main_Choose_Game(self):
        os.system("Call_UI_ChooseGame.py")

    def Open_Main_Top(self):
        os.system("Call_UI_TopGame.py")


    def Close_Win(self):
        sys.exit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Welcome()
    win.setStyleSheet("#MainWindow{border-image:url(./backimg.png);}")
    win.show()
    sys.exit(app.exec_())