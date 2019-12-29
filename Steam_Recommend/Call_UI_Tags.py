import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_Tags import Ui_MainWindow
import Prog_SteamFixed



class Main_Tags( QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(Main_Tags,self).__init__()
        self.setupUi(self)
        Button_Close = QPushButton(self)
        Button_Close.setObjectName('Button_Close')
        Button_Close.setGeometry(QtCore.QRect(1092+317, 10, 19, 19))
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
        Button_Mini.setGeometry(QtCore.QRect(1067+317, 10, 19, 19))
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

    def show_game(self,code):
        lst_game = Prog_SteamFixed.infoAnalysis(self.lst_tag[code])
        self.w1_name.setText(lst_game[0]['Gamename'])
        self.w1_rr_text.setText(lst_game[0]['Recent Reviews'])
        self.w1_or_text.setText(lst_game[0]['Overall Reviews'])
        self.w1_tag_text.setText(lst_game[0]['Tag'])
        self.w1_price.setText(lst_game[0]['Price'])
        self.w1_dev_text.setText(lst_game[0]['Developer'])
        self.w1_ds_text.setText(lst_game[0]['Description'])
        te_img = QImage('tag_logo1.jpg')
        res_img = te_img.scaled(310,145,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.w1_img.setPixmap(QPixmap(res_img))

        self.w2_name.setText(lst_game[1]['Gamename'])
        self.w2_rr_text.setText(lst_game[1]['Recent Reviews'])
        self.w2_or_text.setText(lst_game[1]['Overall Reviews'])
        self.w2_tag_text.setText(lst_game[1]['Tag'])
        self.w2_price.setText(lst_game[1]['Price'])
        self.w2_dev_text.setText(lst_game[1]['Developer'])
        self.w2_ds_text.setText(lst_game[1]['Description'])
        self.w2_img.setPixmap(QPixmap('logo2.jpg'))
        te_img = QImage('tag_logo2.jpg')
        res_img = te_img.scaled(310,145,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.w2_img.setPixmap(QPixmap(res_img))

        self.w3_name.setText(lst_game[2]['Gamename'])
        self.w3_rr_text.setText(lst_game[2]['Recent Reviews'])
        self.w3_or_text.setText(lst_game[2]['Overall Reviews'])
        self.w3_tag_text.setText(lst_game[2]['Tag'])
        self.w3_price.setText(lst_game[2]['Price'])
        self.w3_dev_text.setText(lst_game[2]['Developer'])
        self.w3_ds_text.setText(lst_game[2]['Description'])
        te_img = QImage('tag_logo3.jpg')
        res_img = te_img.scaled(310,145,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.w3_img.setPixmap(QPixmap(res_img))

        self.w4_name.setText(lst_game[3]['Gamename'])
        self.w4_rr_text.setText(lst_game[3]['Recent Reviews'])
        self.w4_or_text.setText(lst_game[3]['Overall Reviews'])
        self.w4_tag_text.setText(lst_game[3]['Tag'])
        self.w4_price.setText(lst_game[3]['Price'])
        self.w4_dev_text.setText(lst_game[3]['Developer'])
        self.w4_ds_text.setText(lst_game[3]['Description'])
        te_img = QImage('tag_logo4.jpg')
        res_img = te_img.scaled(310,145,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.w4_img.setPixmap(QPixmap(res_img))

        self.w5_name.setText(lst_game[4]['Gamename'])
        self.w5_rr_text.setText(lst_game[4]['Recent Reviews'])
        self.w5_or_text.setText(lst_game[4]['Overall Reviews'])
        self.w5_tag_text.setText(lst_game[4]['Tag'])
        self.w5_price.setText(lst_game[4]['Price'])
        self.w5_dev_text.setText(lst_game[4]['Developer'])
        self.w5_ds_text.setText(lst_game[4]['Description'])
        te_img = QImage('tag_logo5.jpg')
        res_img = te_img.scaled(310,145,Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.w5_img.setPixmap(QPixmap(res_img))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Main_Tags()
    win.setStyleSheet("#MainWindow{border-image:url(./backimg_tags.png);}")
    win.show()
    sys.exit(app.exec_())