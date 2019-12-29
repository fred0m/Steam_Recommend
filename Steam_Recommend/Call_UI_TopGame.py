import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_TopGame import Ui_MainWindow
import Prog_SteamFixed

class Main_Top( QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(Main_Top,self).__init__()
        self.setupUi(self)
        Button_Close = QPushButton(self)
        Button_Close.setObjectName('Button_Close')
        Button_Close.setGeometry(QtCore.QRect(1092 + 317, 10, 19, 19))
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
        Button_Mini.setGeometry(QtCore.QRect(1067 + 317, 10, 19, 19))
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
    def show_game(self):
        lst_game = Prog_SteamFixed.anotherTag()
        self.tw1_name.setText(lst_game[0]['Gamename'])
        self.tw1_or_text.setText(lst_game[0]['Overall Reviews'])
        self.tw1_tags_text.setText(lst_game[0]['Tag'])
        self.tw1_price.setText(lst_game[0]['Price'])
        self.tw1_dev.setText(lst_game[0]['Developer'])
        te_img = QImage('top_logo1.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.tw1_img.setPixmap(QPixmap(res_img))

        self.tw2_name.setText(lst_game[1]['Gamename'])
        self.tw2_or_text.setText(lst_game[1]['Overall Reviews'])
        self.tw2_tags_text.setText(lst_game[1]['Tag'])
        self.tw2_price.setText(lst_game[1]['Price'])
        self.tw2_dev.setText(lst_game[1]['Developer'])
        te_img = QImage('top_logo2.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.tw2_img.setPixmap(QPixmap(res_img))

        self.tw3_name.setText(lst_game[2]['Gamename'])
        self.tw3_or_text.setText(lst_game[2]['Overall Reviews'])
        self.tw3_tags_text.setText(lst_game[2]['Tag'])
        self.tw3_price.setText(lst_game[2]['Price'])
        self.tw3_dev.setText(lst_game[2]['Developer'])
        te_img = QImage('top_logo3.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.tw3_img.setPixmap(QPixmap(res_img))

        self.tw4_name.setText(lst_game[3]['Gamename'])
        self.tw4_or_text.setText(lst_game[3]['Overall Reviews'])
        self.tw4_tags_text.setText(lst_game[3]['Tag'])
        self.tw4_price.setText(lst_game[3]['Price'])
        self.tw4_dev.setText(lst_game[3]['Developer'])
        te_img = QImage('top_logo4.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.tw4_img.setPixmap(QPixmap(res_img))

        self.tw5_name.setText(lst_game[4]['Gamename'])
        self.tw5_or_text.setText(lst_game[4]['Overall Reviews'])
        self.tw5_tags_text.setText(lst_game[4]['Tag'])
        self.tw5_price.setText(lst_game[4]['Price'])
        self.tw5_dev.setText(lst_game[4]['Developer'])
        te_img = QImage('top_logo5.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.tw5_img.setPixmap(QPixmap(res_img))

        self.tw6_name.setText(lst_game[5]['Gamename'])
        self.tw6_or_text.setText(lst_game[5]['Overall Reviews'])
        self.tw6_tags_text.setText(lst_game[5]['Tag'])
        self.tw6_price.setText(lst_game[5]['Price'])

        self.tw7_name.setText(lst_game[6]['Gamename'])
        self.tw7_or_text.setText(lst_game[6]['Overall Reviews'])
        self.tw7_tags_text.setText(lst_game[6]['Tag'])
        self.tw7_price.setText(lst_game[6]['Price'])

        self.tw8_name.setText(lst_game[7]['Gamename'])
        self.tw8_or_text.setText(lst_game[7]['Overall Reviews'])
        self.tw8_tags_text.setText(lst_game[7]['Tag'])
        self.tw8_price.setText(lst_game[7]['Price'])

        self.tw9_name.setText(lst_game[8]['Gamename'])
        self.tw9_or_text.setText(lst_game[8]['Overall Reviews'])
        self.tw9_tags_text.setText(lst_game[8]['Tag'])
        self.tw9_price.setText(lst_game[8]['Price'])

        self.tw10_name.setText(lst_game[9]['Gamename'])
        self.tw10_or_text.setText(lst_game[9]['Overall Reviews'])
        self.tw10_tags_text.setText(lst_game[9]['Tag'])
        self.tw10_price.setText(lst_game[9]['Price'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main_Top()
    win.setStyleSheet("#MainWindow{border-image:url(./backimg_top.png);}")
    win.show()
    win.show_game()
    sys.exit(app.exec_())