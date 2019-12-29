import sys
from PyQt5.QtWidgets import QApplication , QMainWindow, QWidget , QFileDialog
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from UI_ChooseGame import Ui_MainWindow
import Prog_GameRecommend
import Prog_imgGeter
import Prog_GetURLbyName
import Prog_randomGameGeter
import Es
import time
import Tool_Cleanner

#定义全局变量：选择计数器
ch_count = 0

class Main_Choose_Game( QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(Main_Choose_Game,self).__init__()
        self.setupUi(self)
        self.lst_name_class = []
        self.lst_name_chosen = ['unknow','unknow','unknow']
        self.lst_name_calcu = []
        self.Grandom = Prog_randomGameGeter.randomGameGeter()
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
        self.cw1_checkBox.stateChanged.connect(self.cb1)
        self.cw2_checkBox.stateChanged.connect(self.cb2)
        self.cw3_checkBox.stateChanged.connect(self.cb3)
        self.cw4_checkBox.stateChanged.connect(self.cb4)
        self.cw5_checkBox.stateChanged.connect(self.cb5)
        self.cw6_checkBox.stateChanged.connect(self.cb6)
        self.Button_back.clicked.connect(lambda:self.reset())
        self.Button_go.clicked.connect(lambda:self.calcu_game())
        self.Button_reflash.clicked.connect(lambda:self.reflash_cw_game())

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
    def check(self):
        global ch_count
        if ch_count >= 0 and ch_count < 3:
            self.Button_back.setEnabled(True)
            self.Button_go.setEnabled(False)
            self.cw1_checkBox.setEnabled(True)
            self.cw2_checkBox.setEnabled(True)
            self.cw3_checkBox.setEnabled(True)
            self.cw4_checkBox.setEnabled(True)
            self.cw5_checkBox.setEnabled(True)
            self.cw6_checkBox.setEnabled(True)
        if ch_count >= 3:
            self.Button_back.setEnabled(True)
            self.Button_go.setEnabled(True)
            self.cw1_checkBox.setEnabled(False)
            self.cw2_checkBox.setEnabled(False)
            self.cw3_checkBox.setEnabled(False)
            self.cw4_checkBox.setEnabled(False)
            self.cw5_checkBox.setEnabled(False)
            self.cw6_checkBox.setEnabled(False)
    def add_game(self,num,name):
        if num == 1:
            self.hw1_name.setText(name)
            self.hw1_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[0] = name
        if num == 2:
            self.hw2_name.setText(name)
            self.hw2_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[1] = name
        if num == 3:
            self.hw3_name.setText(name)
            self.hw3_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[2] = name
    def del_game(self,num):
        if num == 1:
            self.hw1_name.setText("Unknow")
            self.hw1_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[0] = 'unknow'
        if num == 2:
            self.hw2_name.setText("Unknow")
            self.hw2_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[1] = 'unknow'
        if num == 3:
            self.hw3_name.setText("Unknow")
            self.hw3_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[2] = 'unknow'
    def reset(self):
        global ch_count
        print(self.lst_name_chosen)
        self.hw1_name.setText("Unknow")
        self.hw1_name.setStyleSheet("color:#464e5c")
        self.hw2_name.setText("Unknow")
        self.hw2_name.setStyleSheet("color:#464e5c")
        self.hw3_name.setText("Unknow")
        self.hw3_name.setStyleSheet("color:#464e5c")
        self.lst_name_chosen[0] = 'unknow'
        self.lst_name_chosen[1] = 'unknow'
        self.lst_name_chosen[2] = 'unknow'
        self.lst_name_calcu.clear()
        self.Button_go.setEnabled(False)
        self.cw1_checkBox.setEnabled(True)
        self.cw2_checkBox.setEnabled(True)
        self.cw3_checkBox.setEnabled(True)
        self.cw4_checkBox.setEnabled(True)
        self.cw5_checkBox.setEnabled(True)
        self.cw6_checkBox.setEnabled(True)
        self.cw1_checkBox.setChecked(False)
        self.cw2_checkBox.setChecked(False)
        self.cw3_checkBox.setChecked(False)
        self.cw4_checkBox.setChecked(False)
        self.cw5_checkBox.setChecked(False)
        self.cw6_checkBox.setChecked(False)
        ch_count = 0
    def calcu_game(self):
        try:
            self.lst_name_calcu = Prog_GameRecommend.GetGame(self.lst_name_chosen)
            print(self.lst_name_calcu)
            self.show_rw_game()
        except:
            self.rw_error_none()
    def rw_error_none(self):
        self.rw1_name.setText('ERROR: Getting Game Failed')
        self.rw1_dev.setText('Plaese choose your game again')
        self.rw1_tags_text.setText('Unknow')
        self.rw1_or_text.setText('Unknow')
        self.rw1_price.setText('Unknow')
        self.rw2_name.setText('ERROR: Getting Game Failed')
        self.rw2_dev.setText('Plaese choose your game again')
        self.rw2_tags_text.setText('Unknow')
        self.rw2_or_text.setText('Unknow')
        self.rw2_price.setText('Unknow')
        self.rw3_name.setText('ERROR: Getting Game Failed')
        self.rw3_dev.setText('Plaese choose your game again')
        self.rw3_tags_text.setText('Unknow')
        self.rw3_or_text.setText('Unknow')
        self.rw3_price.setText('Unknow')
    def show_rw_game(self):
        lst_name = self.lst_name_calcu

        lst_game = []
        n = 4
        num = 0

        for i in range(0,n):
            try:
                print("name: " + str(lst_name[i]))
                url_g = Prog_GetURLbyName.GetURL(str(lst_name[i]))
                print("url: " + str(url_g))
                data_g = Es.detailsDataGeter(url_g)
                data_g.detailsGeterFixed()
                print("info: " + str(data_g.data))
                img_g = Prog_imgGeter.imgGeter(url_g)
                img_g.saveImg(img_g.getHeaderImg(),'RGlogo' + str(num))
                lst_game.append(data_g.data)
                print("success")
                num += 1
            except:
                n += 1
                print("error in: " + str(lst_name[i]))
                continue
            if (num >= 3):
                break

        print(lst_game)
        temp_dict = {'Gamename': 'Getting Game Failed', 'Developer': 'Plaese choose your game again',
                     'Recent Reviews': 'Unknow', 'Overall Reviews': 'Unknow', 'Description': 'Unknow',
                     'Price': 'Unknow', 'Tag': 'Unknow'}
        for j in range(3):
            lst_game.append(temp_dict)
        print(lst_game)

        self.rw1_name.setText(lst_game[0]['Gamename'])
        self.rw1_dev.setText(lst_game[0]['Developer'])
        self.rw1_tags_text.setText(lst_game[0]['Tag'])
        self.rw1_or_text.setText(lst_game[0]['Overall Reviews'])
        self.rw1_price.setText(lst_game[0]['Price'])


        te_img = QImage('RGlogo0.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.rw1_img.setPixmap(QPixmap(res_img))

        
        self.rw2_name.setText(lst_game[1]['Gamename'])
        self.rw2_dev.setText(lst_game[1]['Developer'])
        self.rw2_tags_text.setText(lst_game[1]['Tag'])
        self.rw2_or_text.setText(lst_game[1]['Overall Reviews'])
        self.rw2_price.setText(lst_game[1]['Price'])
        te_img = QImage('RGlogo1.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.rw2_img.setPixmap(QPixmap(res_img))

        self.rw3_name.setText(lst_game[2]['Gamename'])
        self.rw3_dev.setText(lst_game[2]['Developer'])
        self.rw3_tags_text.setText(lst_game[2]['Tag'])
        self.rw3_or_text.setText(lst_game[2]['Overall Reviews'])
        self.rw3_price.setText(lst_game[2]['Price'])
        te_img = QImage('RGlogo2.jpg')
        res_img = te_img.scaled(260, 121, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.rw3_img.setPixmap(QPixmap(res_img))
    def cb1(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[0]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def cb2(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[1]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def cb3(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[2]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def cb4(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[3]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def cb5(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[4]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def cb6(self,state):
        global ch_count
        if state == Qt.Checked:
            ch_count += 1
            self.add_game(ch_count, str(self.lst_name_class[5]))
        else:
            self.del_game(ch_count)
            ch_count -= 1
        self.check()
    def reflash_cw_game(self):
        Tool_Cleanner.cleanimg()
        global ch_count
        self.Grandom.reflash()
        lst_name = self.Grandom.get()     #给出11个游戏的名称
        lst_game = []
        lst_useful_name = []
        lst_output = []
        n = 7
        num = 0
        for i in range(0,n):
            try:
                print("name: " + str(lst_name[i]))
                url_game = Prog_GetURLbyName.GetURL(str(lst_name[i]))
                print("url: " + str(url_game))
                data_game = Es.detailsDataGeter(url_game)
                data_game.detailsGeterFixed()
                print("info: " + str(data_game.data))
                img_game = Prog_imgGeter.imgGeter(url_game)
                img_game.saveImg(img_game.getHeaderImg(),'CGlogo' + str(num))
                lst_useful_name.append(lst_name[i])
                lst_game.append(data_game.data)
                num += 1
            except:
                n += 1
                print("----error in: " + str(lst_name[i]))
                continue
            if(num == 6):
                break
        temp_dict = {'Gamename': 'Getting Game Failed', 'Developer': 'Plaese choose your game again',
                     'Recent Reviews': 'Unknow', 'Overall Reviews': 'Unknow', 'Description': 'Unknow',
                     'Price': 'Unknow', 'Tag': 'Unknow'}
        for j in range(6):
            lst_game.append(temp_dict)
        print(lst_game)
        lst_output.append(lst_useful_name)
        lst_output.append(lst_game)
        lst_output.append(num)
        self.show_cw_game(lst_output)
        te_num = ch_count
        te_str1 = self.hw1_name.text()
        te_str2 = self.hw2_name.text()
        te_str3 = self.hw3_name.text()
        self.cw1_checkBox.setChecked(False)
        self.cw2_checkBox.setChecked(False)
        self.cw3_checkBox.setChecked(False)
        self.cw4_checkBox.setChecked(False)
        self.cw5_checkBox.setChecked(False)
        self.cw6_checkBox.setChecked(False)
        ch_count = te_num
        self.hw1_name.setText(te_str1)
        self.hw2_name.setText(te_str2)
        self.hw3_name.setText(te_str3)
        if te_str1 == 'Unknow':
            self.hw1_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[0] = 'unknow'
        else:
            self.hw1_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[0] = te_str1

        if te_str2 == 'Unknow':
            self.hw2_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[1] = 'unknow'
        else:
            self.hw2_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[1] = te_str1

        if te_str1 == 'Unknow':
            self.hw3_name.setStyleSheet("color:#464e5c")
            self.lst_name_chosen[2] = 'unknow'
        else:
            self.hw3_name.setStyleSheet("color:#bad3e0")
            self.lst_name_chosen[2] = te_str1



    def get_cw_game(self):
        lst_name = self.Grandom.get()   #给出11个游戏的名称
        lst_game = []
        lst_useful_name = []
        lst_output = []
        n = 7
        num = 0
        for i in range(0,n):
            try:
                print("name: " + str(lst_name[i]))
                url_game = Prog_GetURLbyName.GetURL(str(lst_name[i]))
                print("url: " + str(url_game))
                data_game = Es.detailsDataGeter(url_game)
                data_game.detailsGeterFixed()
                print("info: " + str(data_game.data))
                img_game = Prog_imgGeter.imgGeter(url_game)
                img_game.saveImg(img_game.getHeaderImg(),'CGlogo' + str(num))
                lst_useful_name.append(lst_name[i])
                lst_game.append(data_game.data)
                num += 1
            except:
                n += 1
                print("----error in: " + str(lst_name[i]))
                continue
            if(num == 6):
                break
        temp_dict = {'Gamename': 'Getting Game Failed', 'Developer': 'Plaese choose your game again',
                     'Recent Reviews': 'Unknow', 'Overall Reviews': 'Unknow', 'Description': 'Unknow',
                     'Price': 'Unknow', 'Tag': 'Unknow'}
        for j in range(6):
            lst_game.append(temp_dict)
        print(lst_game)
        lst_output.append(lst_useful_name)
        lst_output.append(lst_game)
        lst_output.append(num)
        return lst_output
    def show_cw_game(self,lst_input):
        lst_game = lst_input[1]
        self.lst_name_class = lst_input[0]
        self.cw1_name.setText(lst_game[0]['Gamename'])
        te_img = QImage('CGlogo0.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw1_img.setPixmap(QPixmap(res_img))

        self.cw2_name.setText(lst_game[1]['Gamename'])
        te_img = QImage('CGlogo1.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw2_img.setPixmap(QPixmap(res_img))

        self.cw3_name.setText(lst_game[2]['Gamename'])
        te_img = QImage('CGlogo2.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw3_img.setPixmap(QPixmap(res_img))

        self.cw4_name.setText(lst_game[3]['Gamename'])
        te_img = QImage('CGlogo3.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw4_img.setPixmap(QPixmap(res_img))

        self.cw5_name.setText(lst_game[4]['Gamename'])
        te_img = QImage('CGlogo4.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw5_img.setPixmap(QPixmap(res_img))

        self.cw6_name.setText(lst_game[5]['Gamename'])
        te_img = QImage('CGlogo5.jpg')
        res_img = te_img.scaled(246, 115, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.cw6_img.setPixmap(QPixmap(res_img))
if __name__ == '__main__':
    Tool_Cleanner.cleanimg()
    app = QApplication(sys.argv)
    win = Main_Choose_Game()
    win.setStyleSheet("#MainWindow{border-image:url(./backimg_tags.png);}")
    win.check()
    win.show()
    time.sleep(1)
    lst_input = win.get_cw_game()
    win.show_cw_game(lst_input)


    sys.exit(app.exec_())

    '''
    random_game = Prog_randomGameGeter()
    lst_name = random_game.get()
    print(lst_name)
    print(lst_name[2])
    dict_game = Prog_GetURLbyName.GetInfo(lst_name[2])
    print(dict_game)
    print(Prog_GetURLbyName.GetURL('Assassins Creed Unity'))
    '''