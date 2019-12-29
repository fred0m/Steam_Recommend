# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main_Tags.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 1000)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1440, 1000))
        MainWindow.setMaximumSize(QtCore.QSize(1440, 1000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../timg.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.w_tags = QtWidgets.QWidget(self.centralwidget)
        self.lst_tag = ['宝藏游戏', '最傻逼的100个dio游戏', '2d(150)', '4人本地游玩(寝室推荐)', '动作', '动作类角色扮演', '动作冒险', '冒险', '动漫', '街机游戏', '氛围游戏',
                '建筑游戏', '弹幕类游戏', '卡牌游戏', '休闲游戏', '多结局类游戏(选择分支)', '经典游戏', '合作游戏', '色彩丰富', '喜剧游戏', '竞技游戏', '可以连接手柄的游戏',
                '可创造', '可爱', '阴暗', '硬核游戏', '地牢探险', '仍在开发的', '探索', 'FPS', '家庭游戏', '幻想', '快节奏', '女主角', '格斗', '第一人称',
                '免费游玩', '有趣', '暴力血腥', '游戏音乐好听', '砍杀', '寻找隐藏(星际玩家慎选)', '历史', '恐怖', '独立游戏', '日系RPG', '本地合作', '本地多人',
                '管理经营', '大型多人在线', '杰作', '成人游戏', '玩梗', '极简', '多人', '音乐', '神秘', '有裸体(黄油)', '在线合作', '开放世界', '物理引擎', '像素风格',
                '平台''点按', '随机地图', '心里恐怖(精神污染)', '解谜', '平台解密', 'PvP', 'RPG', '实时战略', '基于RPGmaker', '竞速', '现实', '放松',
                '值得重玩', '复古', 'Rogue-like', 'Rogue-lite', '沙盒', '科幻', '性', '赶尽杀绝', '射击', '流程短', 'Side,Scroller', '模拟',
                '单人', '太空', '运动', '潜行', '剧情丰富', '策略', '生存', '生存恐怖', '战术', 'Top-Down(层层推进)', '第三人称', '塔防', '回合制',
                '回合制策略', '暴力', '视觉小说(文字类冒险)', '行走模拟器', '战争', '僵尸', '正在打折']
        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(210, 4260)

        self.b0 = QPushButton(self.topFiller)
        self.b0.setText(self.lst_tag[0])
        self.b0.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                                       "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                                       "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b0.setGeometry(QtCore.QRect(10, 10 + 40 * 0, 200, 30))
        self.b0.clicked.connect(lambda: self.show_game(0))

        self.b1 = QPushButton(self.topFiller)
        self.b1.setText(self.lst_tag[1])
        self.b1.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b1.setGeometry(QtCore.QRect(10, 10 + 40 * 1, 200, 30))
        self.b1.clicked.connect(lambda: self.show_game(1))

        self.b2 = QPushButton(self.topFiller)
        self.b2.setText(self.lst_tag[2])
        self.b2.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b2.setGeometry(QtCore.QRect(10, 10 + 40 * 2, 200, 30))
        self.b2.clicked.connect(lambda: self.show_game(2))

        self.b3 = QPushButton(self.topFiller)
        self.b3.setText(self.lst_tag[3])
        self.b3.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b3.setGeometry(QtCore.QRect(10, 10 + 40 * 3, 200, 30))
        self.b3.clicked.connect(lambda: self.show_game(3))

        self.b4 = QPushButton(self.topFiller)
        self.b4.setText(self.lst_tag[4])
        self.b4.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b4.setGeometry(QtCore.QRect(10, 10 + 40 * 4, 200, 30))
        self.b4.clicked.connect(lambda: self.show_game(4))

        self.b5 = QPushButton(self.topFiller)
        self.b5.setText(self.lst_tag[5])
        self.b5.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b5.setGeometry(QtCore.QRect(10, 10 + 40 * 5, 200, 30))
        self.b5.clicked.connect(lambda: self.show_game(5))

        self.b6 = QPushButton(self.topFiller)
        self.b6.setText(self.lst_tag[6])
        self.b6.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b6.setGeometry(QtCore.QRect(10, 10 + 40 * 6, 200, 30))
        self.b6.clicked.connect(lambda: self.show_game(6))

        self.b7 = QPushButton(self.topFiller)
        self.b7.setText(self.lst_tag[7])
        self.b7.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b7.setGeometry(QtCore.QRect(10, 10 + 40 * 7, 200, 30))
        self.b7.clicked.connect(lambda: self.show_game(7))

        self.b8 = QPushButton(self.topFiller)
        self.b8.setText(self.lst_tag[8])
        self.b8.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b8.setGeometry(QtCore.QRect(10, 10 + 40 * 8, 200, 30))
        self.b8.clicked.connect(lambda: self.show_game(8))

        self.b9 = QPushButton(self.topFiller)
        self.b9.setText(self.lst_tag[9])
        self.b9.setStyleSheet("QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
                              "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
                              "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b9.setGeometry(QtCore.QRect(10, 10 + 40 * 9, 200, 30))
        self.b9.clicked.connect(lambda: self.show_game(9))

        self.b10 = QPushButton(self.topFiller)
        self.b10.setText(self.lst_tag[10])
        self.b10.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b10.setGeometry(QtCore.QRect(10, 10 + 40 * 10, 200, 30))
        self.b10.clicked.connect(lambda: self.show_game(10))

        self.b11 = QPushButton(self.topFiller)
        self.b11.setText(self.lst_tag[11])
        self.b11.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b11.setGeometry(QtCore.QRect(10, 10 + 40 * 11, 200, 30))
        self.b11.clicked.connect(lambda: self.show_game(11))

        self.b12 = QPushButton(self.topFiller)
        self.b12.setText(self.lst_tag[12])
        self.b12.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b12.setGeometry(QtCore.QRect(10, 10 + 40 * 12, 200, 30))
        self.b12.clicked.connect(lambda: self.show_game(12))

        self.b13 = QPushButton(self.topFiller)
        self.b13.setText(self.lst_tag[13])
        self.b13.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b13.setGeometry(QtCore.QRect(10, 10 + 40 * 13, 200, 30))
        self.b13.clicked.connect(lambda: self.show_game(13))

        self.b14 = QPushButton(self.topFiller)
        self.b14.setText(self.lst_tag[14])
        self.b14.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b14.setGeometry(QtCore.QRect(10, 10 + 40 * 14, 200, 30))
        self.b14.clicked.connect(lambda: self.show_game(14))

        self.b15 = QPushButton(self.topFiller)
        self.b15.setText(self.lst_tag[15])
        self.b15.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b15.setGeometry(QtCore.QRect(10, 10 + 40 * 15, 200, 30))
        self.b15.clicked.connect(lambda: self.show_game(15))

        self.b16 = QPushButton(self.topFiller)
        self.b16.setText(self.lst_tag[16])
        self.b16.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b16.setGeometry(QtCore.QRect(10, 10 + 40 * 16, 200, 30))
        self.b16.clicked.connect(lambda: self.show_game(16))

        self.b17 = QPushButton(self.topFiller)
        self.b17.setText(self.lst_tag[17])
        self.b17.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b17.setGeometry(QtCore.QRect(10, 10 + 40 * 17, 200, 30))
        self.b17.clicked.connect(lambda: self.show_game(17))

        self.b18 = QPushButton(self.topFiller)
        self.b18.setText(self.lst_tag[18])
        self.b18.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b18.setGeometry(QtCore.QRect(10, 10 + 40 * 18, 200, 30))
        self.b18.clicked.connect(lambda: self.show_game(18))

        self.b19 = QPushButton(self.topFiller)
        self.b19.setText(self.lst_tag[19])
        self.b19.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b19.setGeometry(QtCore.QRect(10, 10 + 40 * 19, 200, 30))
        self.b19.clicked.connect(lambda: self.show_game(19))

        self.b20 = QPushButton(self.topFiller)
        self.b20.setText(self.lst_tag[20])
        self.b20.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b20.setGeometry(QtCore.QRect(10, 10 + 40 * 20, 200, 30))
        self.b20.clicked.connect(lambda: self.show_game(20))

        self.b21 = QPushButton(self.topFiller)
        self.b21.setText(self.lst_tag[21])
        self.b21.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b21.setGeometry(QtCore.QRect(10, 10 + 40 * 21, 200, 30))
        self.b21.clicked.connect(lambda: self.show_game(21))

        self.b22 = QPushButton(self.topFiller)
        self.b22.setText(self.lst_tag[22])
        self.b22.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b22.setGeometry(QtCore.QRect(10, 10 + 40 * 22, 200, 30))
        self.b22.clicked.connect(lambda: self.show_game(22))

        self.b23 = QPushButton(self.topFiller)
        self.b23.setText(self.lst_tag[23])
        self.b23.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b23.setGeometry(QtCore.QRect(10, 10 + 40 * 23, 200, 30))
        self.b23.clicked.connect(lambda: self.show_game(23))

        self.b24 = QPushButton(self.topFiller)
        self.b24.setText(self.lst_tag[24])
        self.b24.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b24.setGeometry(QtCore.QRect(10, 10 + 40 * 24, 200, 30))
        self.b24.clicked.connect(lambda: self.show_game(24))

        self.b25 = QPushButton(self.topFiller)
        self.b25.setText(self.lst_tag[25])
        self.b25.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b25.setGeometry(QtCore.QRect(10, 10 + 40 * 25, 200, 30))
        self.b25.clicked.connect(lambda: self.show_game(25))

        self.b26 = QPushButton(self.topFiller)
        self.b26.setText(self.lst_tag[26])
        self.b26.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b26.setGeometry(QtCore.QRect(10, 10 + 40 * 26, 200, 30))
        self.b26.clicked.connect(lambda: self.show_game(26))

        self.b27 = QPushButton(self.topFiller)
        self.b27.setText(self.lst_tag[27])
        self.b27.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b27.setGeometry(QtCore.QRect(10, 10 + 40 * 27, 200, 30))
        self.b27.clicked.connect(lambda: self.show_game(27))

        self.b28 = QPushButton(self.topFiller)
        self.b28.setText(self.lst_tag[28])
        self.b28.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b28.setGeometry(QtCore.QRect(10, 10 + 40 * 28, 200, 30))
        self.b28.clicked.connect(lambda: self.show_game(28))

        self.b29 = QPushButton(self.topFiller)
        self.b29.setText(self.lst_tag[29])
        self.b29.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b29.setGeometry(QtCore.QRect(10, 10 + 40 * 29, 200, 30))
        self.b29.clicked.connect(lambda: self.show_game(29))

        self.b30 = QPushButton(self.topFiller)
        self.b30.setText(self.lst_tag[30])
        self.b30.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b30.setGeometry(QtCore.QRect(10, 10 + 40 * 30, 200, 30))
        self.b30.clicked.connect(lambda: self.show_game(30))

        self.b31 = QPushButton(self.topFiller)
        self.b31.setText(self.lst_tag[31])
        self.b31.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b31.setGeometry(QtCore.QRect(10, 10 + 40 * 31, 200, 30))
        self.b31.clicked.connect(lambda: self.show_game(31))

        self.b32 = QPushButton(self.topFiller)
        self.b32.setText(self.lst_tag[32])
        self.b32.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b32.setGeometry(QtCore.QRect(10, 10 + 40 * 32, 200, 30))
        self.b32.clicked.connect(lambda: self.show_game(32))

        self.b33 = QPushButton(self.topFiller)
        self.b33.setText(self.lst_tag[33])
        self.b33.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b33.setGeometry(QtCore.QRect(10, 10 + 40 * 33, 200, 30))
        self.b33.clicked.connect(lambda: self.show_game(33))

        self.b34 = QPushButton(self.topFiller)
        self.b34.setText(self.lst_tag[34])
        self.b34.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b34.setGeometry(QtCore.QRect(10, 10 + 40 * 34, 200, 30))
        self.b34.clicked.connect(lambda: self.show_game(34))

        self.b35 = QPushButton(self.topFiller)
        self.b35.setText(self.lst_tag[35])
        self.b35.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b35.setGeometry(QtCore.QRect(10, 10 + 40 * 35, 200, 30))
        self.b35.clicked.connect(lambda: self.show_game(35))

        self.b36 = QPushButton(self.topFiller)
        self.b36.setText(self.lst_tag[36])
        self.b36.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b36.setGeometry(QtCore.QRect(10, 10 + 40 * 36, 200, 30))
        self.b36.clicked.connect(lambda: self.show_game(36))

        self.b37 = QPushButton(self.topFiller)
        self.b37.setText(self.lst_tag[37])
        self.b37.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b37.setGeometry(QtCore.QRect(10, 10 + 40 * 37, 200, 30))
        self.b37.clicked.connect(lambda: self.show_game(37))

        self.b38 = QPushButton(self.topFiller)
        self.b38.setText(self.lst_tag[38])
        self.b38.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b38.setGeometry(QtCore.QRect(10, 10 + 40 * 38, 200, 30))
        self.b38.clicked.connect(lambda: self.show_game(38))

        self.b39 = QPushButton(self.topFiller)
        self.b39.setText(self.lst_tag[39])
        self.b39.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b39.setGeometry(QtCore.QRect(10, 10 + 40 * 39, 200, 30))
        self.b39.clicked.connect(lambda: self.show_game(39))

        self.b40 = QPushButton(self.topFiller)
        self.b40.setText(self.lst_tag[40])
        self.b40.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b40.setGeometry(QtCore.QRect(10, 10 + 40 * 40, 200, 30))
        self.b40.clicked.connect(lambda: self.show_game(40))

        self.b41 = QPushButton(self.topFiller)
        self.b41.setText(self.lst_tag[41])
        self.b41.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b41.setGeometry(QtCore.QRect(10, 10 + 40 * 41, 200, 30))
        self.b41.clicked.connect(lambda: self.show_game(41))

        self.b42 = QPushButton(self.topFiller)
        self.b42.setText(self.lst_tag[42])
        self.b42.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b42.setGeometry(QtCore.QRect(10, 10 + 40 * 42, 200, 30))
        self.b42.clicked.connect(lambda: self.show_game(42))

        self.b43 = QPushButton(self.topFiller)
        self.b43.setText(self.lst_tag[43])
        self.b43.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b43.setGeometry(QtCore.QRect(10, 10 + 40 * 43, 200, 30))
        self.b43.clicked.connect(lambda: self.show_game(43))

        self.b44 = QPushButton(self.topFiller)
        self.b44.setText(self.lst_tag[44])
        self.b44.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b44.setGeometry(QtCore.QRect(10, 10 + 40 * 44, 200, 30))
        self.b44.clicked.connect(lambda: self.show_game(44))

        self.b45 = QPushButton(self.topFiller)
        self.b45.setText(self.lst_tag[45])
        self.b45.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b45.setGeometry(QtCore.QRect(10, 10 + 40 * 45, 200, 30))
        self.b45.clicked.connect(lambda: self.show_game(45))

        self.b46 = QPushButton(self.topFiller)
        self.b46.setText(self.lst_tag[46])
        self.b46.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b46.setGeometry(QtCore.QRect(10, 10 + 40 * 46, 200, 30))
        self.b46.clicked.connect(lambda: self.show_game(46))

        self.b47 = QPushButton(self.topFiller)
        self.b47.setText(self.lst_tag[47])
        self.b47.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b47.setGeometry(QtCore.QRect(10, 10 + 40 * 47, 200, 30))
        self.b47.clicked.connect(lambda: self.show_game(47))

        self.b48 = QPushButton(self.topFiller)
        self.b48.setText(self.lst_tag[48])
        self.b48.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b48.setGeometry(QtCore.QRect(10, 10 + 40 * 48, 200, 30))
        self.b48.clicked.connect(lambda: self.show_game(48))

        self.b49 = QPushButton(self.topFiller)
        self.b49.setText(self.lst_tag[49])
        self.b49.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b49.setGeometry(QtCore.QRect(10, 10 + 40 * 49, 200, 30))
        self.b49.clicked.connect(lambda: self.show_game(49))

        self.b50 = QPushButton(self.topFiller)
        self.b50.setText(self.lst_tag[50])
        self.b50.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b50.setGeometry(QtCore.QRect(10, 10 + 40 * 50, 200, 30))
        self.b50.clicked.connect(lambda: self.show_game(50))

        self.b51 = QPushButton(self.topFiller)
        self.b51.setText(self.lst_tag[51])
        self.b51.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b51.setGeometry(QtCore.QRect(10, 10 + 40 * 51, 200, 30))
        self.b51.clicked.connect(lambda: self.show_game(51))

        self.b52 = QPushButton(self.topFiller)
        self.b52.setText(self.lst_tag[52])
        self.b52.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b52.setGeometry(QtCore.QRect(10, 10 + 40 * 52, 200, 30))
        self.b52.clicked.connect(lambda: self.show_game(52))

        self.b53 = QPushButton(self.topFiller)
        self.b53.setText(self.lst_tag[53])
        self.b53.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b53.setGeometry(QtCore.QRect(10, 10 + 40 * 53, 200, 30))
        self.b53.clicked.connect(lambda: self.show_game(53))

        self.b54 = QPushButton(self.topFiller)
        self.b54.setText(self.lst_tag[54])
        self.b54.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b54.setGeometry(QtCore.QRect(10, 10 + 40 * 54, 200, 30))
        self.b54.clicked.connect(lambda: self.show_game(54))

        self.b55 = QPushButton(self.topFiller)
        self.b55.setText(self.lst_tag[55])
        self.b55.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b55.setGeometry(QtCore.QRect(10, 10 + 40 * 55, 200, 30))
        self.b55.clicked.connect(lambda: self.show_game(55))

        self.b56 = QPushButton(self.topFiller)
        self.b56.setText(self.lst_tag[56])
        self.b56.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b56.setGeometry(QtCore.QRect(10, 10 + 40 * 56, 200, 30))
        self.b56.clicked.connect(lambda: self.show_game(56))

        self.b57 = QPushButton(self.topFiller)
        self.b57.setText(self.lst_tag[57])
        self.b57.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b57.setGeometry(QtCore.QRect(10, 10 + 40 * 57, 200, 30))
        self.b57.clicked.connect(lambda: self.show_game(57))

        self.b58 = QPushButton(self.topFiller)
        self.b58.setText(self.lst_tag[58])
        self.b58.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b58.setGeometry(QtCore.QRect(10, 10 + 40 * 58, 200, 30))
        self.b58.clicked.connect(lambda: self.show_game(58))

        self.b59 = QPushButton(self.topFiller)
        self.b59.setText(self.lst_tag[59])
        self.b59.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b59.setGeometry(QtCore.QRect(10, 10 + 40 * 59, 200, 30))
        self.b59.clicked.connect(lambda: self.show_game(59))

        self.b60 = QPushButton(self.topFiller)
        self.b60.setText(self.lst_tag[60])
        self.b60.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b60.setGeometry(QtCore.QRect(10, 10 + 40 * 60, 200, 30))
        self.b60.clicked.connect(lambda: self.show_game(60))

        self.b61 = QPushButton(self.topFiller)
        self.b61.setText(self.lst_tag[61])
        self.b61.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b61.setGeometry(QtCore.QRect(10, 10 + 40 * 61, 200, 30))
        self.b61.clicked.connect(lambda: self.show_game(61))

        self.b62 = QPushButton(self.topFiller)
        self.b62.setText(self.lst_tag[62])
        self.b62.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b62.setGeometry(QtCore.QRect(10, 10 + 40 * 62, 200, 30))
        self.b62.clicked.connect(lambda: self.show_game(62))

        self.b63 = QPushButton(self.topFiller)
        self.b63.setText(self.lst_tag[63])
        self.b63.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b63.setGeometry(QtCore.QRect(10, 10 + 40 * 63, 200, 30))
        self.b63.clicked.connect(lambda: self.show_game(63))

        self.b64 = QPushButton(self.topFiller)
        self.b64.setText(self.lst_tag[64])
        self.b64.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b64.setGeometry(QtCore.QRect(10, 10 + 40 * 64, 200, 30))
        self.b64.clicked.connect(lambda: self.show_game(64))

        self.b65 = QPushButton(self.topFiller)
        self.b65.setText(self.lst_tag[65])
        self.b65.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b65.setGeometry(QtCore.QRect(10, 10 + 40 * 65, 200, 30))
        self.b65.clicked.connect(lambda: self.show_game(65))

        self.b66 = QPushButton(self.topFiller)
        self.b66.setText(self.lst_tag[66])
        self.b66.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b66.setGeometry(QtCore.QRect(10, 10 + 40 * 66, 200, 30))
        self.b66.clicked.connect(lambda: self.show_game(66))

        self.b67 = QPushButton(self.topFiller)
        self.b67.setText(self.lst_tag[67])
        self.b67.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b67.setGeometry(QtCore.QRect(10, 10 + 40 * 67, 200, 30))
        self.b67.clicked.connect(lambda: self.show_game(67))

        self.b68 = QPushButton(self.topFiller)
        self.b68.setText(self.lst_tag[68])
        self.b68.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b68.setGeometry(QtCore.QRect(10, 10 + 40 * 68, 200, 30))
        self.b68.clicked.connect(lambda: self.show_game(68))

        self.b69 = QPushButton(self.topFiller)
        self.b69.setText(self.lst_tag[69])
        self.b69.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b69.setGeometry(QtCore.QRect(10, 10 + 40 * 69, 200, 30))
        self.b69.clicked.connect(lambda: self.show_game(69))

        self.b70 = QPushButton(self.topFiller)
        self.b70.setText(self.lst_tag[70])
        self.b70.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b70.setGeometry(QtCore.QRect(10, 10 + 40 * 70, 200, 30))
        self.b70.clicked.connect(lambda: self.show_game(70))

        self.b71 = QPushButton(self.topFiller)
        self.b71.setText(self.lst_tag[71])
        self.b71.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b71.setGeometry(QtCore.QRect(10, 10 + 40 * 71, 200, 30))
        self.b71.clicked.connect(lambda: self.show_game(71))

        self.b72 = QPushButton(self.topFiller)
        self.b72.setText(self.lst_tag[72])
        self.b72.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b72.setGeometry(QtCore.QRect(10, 10 + 40 * 72, 200, 30))
        self.b72.clicked.connect(lambda: self.show_game(72))

        self.b73 = QPushButton(self.topFiller)
        self.b73.setText(self.lst_tag[73])
        self.b73.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b73.setGeometry(QtCore.QRect(10, 10 + 40 * 73, 200, 30))
        self.b73.clicked.connect(lambda: self.show_game(73))

        self.b74 = QPushButton(self.topFiller)
        self.b74.setText(self.lst_tag[74])
        self.b74.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b74.setGeometry(QtCore.QRect(10, 10 + 40 * 74, 200, 30))
        self.b74.clicked.connect(lambda: self.show_game(74))

        self.b75 = QPushButton(self.topFiller)
        self.b75.setText(self.lst_tag[75])
        self.b75.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b75.setGeometry(QtCore.QRect(10, 10 + 40 * 75, 200, 30))
        self.b75.clicked.connect(lambda: self.show_game(75))

        self.b76 = QPushButton(self.topFiller)
        self.b76.setText(self.lst_tag[76])
        self.b76.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b76.setGeometry(QtCore.QRect(10, 10 + 40 * 76, 200, 30))
        self.b76.clicked.connect(lambda: self.show_game(76))

        self.b77 = QPushButton(self.topFiller)
        self.b77.setText(self.lst_tag[77])
        self.b77.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b77.setGeometry(QtCore.QRect(10, 10 + 40 * 77, 200, 30))
        self.b77.clicked.connect(lambda: self.show_game(77))

        self.b78 = QPushButton(self.topFiller)
        self.b78.setText(self.lst_tag[78])
        self.b78.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b78.setGeometry(QtCore.QRect(10, 10 + 40 * 78, 200, 30))
        self.b78.clicked.connect(lambda: self.show_game(78))

        self.b79 = QPushButton(self.topFiller)
        self.b79.setText(self.lst_tag[79])
        self.b79.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b79.setGeometry(QtCore.QRect(10, 10 + 40 * 79, 200, 30))
        self.b79.clicked.connect(lambda: self.show_game(79))

        self.b80 = QPushButton(self.topFiller)
        self.b80.setText(self.lst_tag[80])
        self.b80.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b80.setGeometry(QtCore.QRect(10, 10 + 40 * 80, 200, 30))
        self.b80.clicked.connect(lambda: self.show_game(80))

        self.b81 = QPushButton(self.topFiller)
        self.b81.setText(self.lst_tag[81])
        self.b81.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b81.setGeometry(QtCore.QRect(10, 10 + 40 * 81, 200, 30))
        self.b81.clicked.connect(lambda: self.show_game(81))

        self.b82 = QPushButton(self.topFiller)
        self.b82.setText(self.lst_tag[82])
        self.b82.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b82.setGeometry(QtCore.QRect(10, 10 + 40 * 82, 200, 30))
        self.b82.clicked.connect(lambda: self.show_game(82))

        self.b83 = QPushButton(self.topFiller)
        self.b83.setText(self.lst_tag[83])
        self.b83.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b83.setGeometry(QtCore.QRect(10, 10 + 40 * 83, 200, 30))
        self.b83.clicked.connect(lambda: self.show_game(83))

        self.b84 = QPushButton(self.topFiller)
        self.b84.setText(self.lst_tag[84])
        self.b84.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b84.setGeometry(QtCore.QRect(10, 10 + 40 * 84, 200, 30))
        self.b84.clicked.connect(lambda: self.show_game(84))

        self.b85 = QPushButton(self.topFiller)
        self.b85.setText(self.lst_tag[85])
        self.b85.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b85.setGeometry(QtCore.QRect(10, 10 + 40 * 85, 200, 30))
        self.b85.clicked.connect(lambda: self.show_game(85))

        self.b86 = QPushButton(self.topFiller)
        self.b86.setText(self.lst_tag[86])
        self.b86.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b86.setGeometry(QtCore.QRect(10, 10 + 40 * 86, 200, 30))
        self.b86.clicked.connect(lambda: self.show_game(86))

        self.b87 = QPushButton(self.topFiller)
        self.b87.setText(self.lst_tag[87])
        self.b87.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b87.setGeometry(QtCore.QRect(10, 10 + 40 * 87, 200, 30))
        self.b87.clicked.connect(lambda: self.show_game(87))

        self.b88 = QPushButton(self.topFiller)
        self.b88.setText(self.lst_tag[88])
        self.b88.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b88.setGeometry(QtCore.QRect(10, 10 + 40 * 88, 200, 30))
        self.b88.clicked.connect(lambda: self.show_game(88))

        self.b89 = QPushButton(self.topFiller)
        self.b89.setText(self.lst_tag[89])
        self.b89.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b89.setGeometry(QtCore.QRect(10, 10 + 40 * 89, 200, 30))
        self.b89.clicked.connect(lambda: self.show_game(89))

        self.b90 = QPushButton(self.topFiller)
        self.b90.setText(self.lst_tag[90])
        self.b90.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b90.setGeometry(QtCore.QRect(10, 10 + 40 * 90, 200, 30))
        self.b90.clicked.connect(lambda: self.show_game(90))

        self.b91 = QPushButton(self.topFiller)
        self.b91.setText(self.lst_tag[91])
        self.b91.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b91.setGeometry(QtCore.QRect(10, 10 + 40 * 91, 200, 30))
        self.b91.clicked.connect(lambda: self.show_game(91))

        self.b92 = QPushButton(self.topFiller)
        self.b92.setText(self.lst_tag[92])
        self.b92.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b92.setGeometry(QtCore.QRect(10, 10 + 40 * 92, 200, 30))
        self.b92.clicked.connect(lambda: self.show_game(92))

        self.b93 = QPushButton(self.topFiller)
        self.b93.setText(self.lst_tag[93])
        self.b93.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b93.setGeometry(QtCore.QRect(10, 10 + 40 * 93, 200, 30))
        self.b93.clicked.connect(lambda: self.show_game(93))

        self.b94 = QPushButton(self.topFiller)
        self.b94.setText(self.lst_tag[94])
        self.b94.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b94.setGeometry(QtCore.QRect(10, 10 + 40 * 94, 200, 30))
        self.b94.clicked.connect(lambda: self.show_game(94))

        self.b95 = QPushButton(self.topFiller)
        self.b95.setText(self.lst_tag[95])
        self.b95.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b95.setGeometry(QtCore.QRect(10, 10 + 40 * 95, 200, 30))
        self.b95.clicked.connect(lambda: self.show_game(95))

        self.b96 = QPushButton(self.topFiller)
        self.b96.setText(self.lst_tag[96])
        self.b96.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b96.setGeometry(QtCore.QRect(10, 10 + 40 * 96, 200, 30))
        self.b96.clicked.connect(lambda: self.show_game(96))

        self.b97 = QPushButton(self.topFiller)
        self.b97.setText(self.lst_tag[97])
        self.b97.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b97.setGeometry(QtCore.QRect(10, 10 + 40 * 97, 200, 30))
        self.b97.clicked.connect(lambda: self.show_game(97))

        self.b98 = QPushButton(self.topFiller)
        self.b98.setText(self.lst_tag[98])
        self.b98.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b98.setGeometry(QtCore.QRect(10, 10 + 40 * 98, 200, 30))
        self.b98.clicked.connect(lambda: self.show_game(98))

        self.b99 = QPushButton(self.topFiller)
        self.b99.setText(self.lst_tag[99])
        self.b99.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b99.setGeometry(QtCore.QRect(10, 10 + 40 * 99, 200, 30))
        self.b99.clicked.connect(lambda: self.show_game(99))

        self.b100 = QPushButton(self.topFiller)
        self.b100.setText(self.lst_tag[100])
        self.b100.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b100.setGeometry(QtCore.QRect(10, 10 + 40 * 100, 200, 30))
        self.b100.clicked.connect(lambda: self.show_game(100))

        self.b101 = QPushButton(self.topFiller)
        self.b101.setText(self.lst_tag[101])
        self.b101.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b101.setGeometry(QtCore.QRect(10, 10 + 40 * 101, 200, 30))
        self.b101.clicked.connect(lambda: self.show_game(101))

        self.b102 = QPushButton(self.topFiller)
        self.b102.setText(self.lst_tag[102])
        self.b102.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b102.setGeometry(QtCore.QRect(10, 10 + 40 * 102, 200, 30))
        self.b102.clicked.connect(lambda: self.show_game(102))

        self.b103 = QPushButton(self.topFiller)
        self.b103.setText(self.lst_tag[103])
        self.b103.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b103.setGeometry(QtCore.QRect(10, 10 + 40 * 103, 200, 30))
        self.b103.clicked.connect(lambda: self.show_game(103))

        self.b104 = QPushButton(self.topFiller)
        self.b104.setText(self.lst_tag[104])
        self.b104.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b104.setGeometry(QtCore.QRect(10, 10 + 40 * 104, 200, 30))
        self.b104.clicked.connect(lambda: self.show_game(104))

        self.b105 = QPushButton(self.topFiller)
        self.b105.setText(self.lst_tag[105])
        self.b105.setStyleSheet(
            "QPushButton{color:white;background-color:#263550;border-style:solid; border-radius:10px}"
            "QPushButton:hover{color:white;background-color:#495976;border-style:solid; border-radius:10px}"
            "QPushButton:Pressed{color:white;background-color:#667288;border-style:solid; border-radius:10px}")
        self.b105.setGeometry(QtCore.QRect(10, 10 + 40 * 105, 200, 30))
        self.b105.clicked.connect(lambda: self.show_game(105))




        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.scroll.setStyleSheet("QScrollBar{background:rgb(0,0,0,0)}"
                                  "QScrollArea QScrollBar::sub-page:vertical{background:rgb(0,0,0,0);border-radius:10px}"
                                  "QScrollArea QScrollBar::add-page:vertical{background:rgb(0,0,0,0);border-radius:10px}"
                                  "QScrollArea QScrollBar::handle:vertical{background:#263550;border-radius:8px}"
                                  "QScrollArea QScrollBar::handle:vertical:hover{background:#495976;border-radius:8px}"
                                  "QScrollArea QScrollBar::sub-line:vertical{background:rgb(0,0,0,0)}"
                                  "QScrollArea QScrollBar::add-line:vertical{background:rgb(0,0,0,0)}")



        #self.scroll.setStyleSheet("border:0px")



        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        self.w_tags.setLayout(self.vbox)
        self.w_tags.setStyleSheet('background:transparent;border:0px')
        self.topFiller.setStyleSheet('background:transparent')
        #self.w_tags.setStyleSheet("backgroun-color:red;border:0px;color:rgb(0,255,0)")
        #self.topFiller.setStyleSheet("backgroun:red;border:0px;color:rgb(0,255,0)")

        self.w_tags.setGeometry(QtCore.QRect(0, 80, 261, 891))
        self.w_tags.setObjectName("w_tags")





        self.w1 = QtWidgets.QWidget(self.centralwidget)
        self.w1.setGeometry(QtCore.QRect(270, 88, 1157, 161))
        self.w1.setObjectName("w1")

        self.w1.setStyleSheet("background-color:#263550;border-radius:15px")

        self.w1_tabWidget = QtWidgets.QTabWidget(self.w1)
        self.w1_tabWidget.setGeometry(QtCore.QRect(330, 10, 821, 140))
        self.w1_tabWidget.setStyleSheet("color:#bad3e0")
        self.w1_tabWidget.setObjectName("w1_tabWidget")
        self.w1_tabWidget.setStyleSheet("QTabWidget::pane{border-width:1px;border-color:rgb(255, 255, 255，160);background: transparent}"
                                        "QTabBar::tab{min-width:75px; min-height:22px;}"
                                        "QTabBar::tab:first:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:15;margin-right:2;}"
                                        "QTabBar::tab:first:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
                                        "QTabBar::tab:first:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
                                        "QTabBar::tab:last:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
                                        "QTabBar::tab:last:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
                                        "QTabBar::tab:last:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}")



        self.w1_tab1 = QtWidgets.QWidget()
        self.w1_tab1.setObjectName("w1_tab1")
        self.w1_tab1.setStyleSheet("background-color:#1c263a")
        self.w1_tab1.setStyleSheet("color:white")
        self.w1_name = QtWidgets.QLabel(self.w1_tab1)
        self.w1_name.setGeometry(QtCore.QRect(10, 10, 641, 40))

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.w1_name.setFont(font)
        self.w1_name.setObjectName("w1_name")
        self.w1_name.setStyleSheet("color:#bad3e0")
        self.w1_rr = QtWidgets.QLabel(self.w1_tab1)
        self.w1_rr.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_rr.setFont(font)
        self.w1_rr.setObjectName("w1_rr")
        self.w1_rr_text = QtWidgets.QLabel(self.w1_tab1)
        self.w1_rr_text.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.w1_rr.setStyleSheet("color:#bad3e0")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_rr_text.setFont(font)
        self.w1_rr_text.setObjectName("w1_rr_text")
        self.w1_rr_text.setStyleSheet("color:#66c0f4")



        self.w1_or = QtWidgets.QLabel(self.w1_tab1)
        self.w1_or.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.w1_or.setStyleSheet("color:#bad3e0")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_or.setFont(font)
        self.w1_or.setObjectName("w1_or")
        self.w1_or_text = QtWidgets.QLabel(self.w1_tab1)
        self.w1_or_text.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.w1_or_text.setStyleSheet("color:#66c0f4")


        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_or_text.setFont(font)
        self.w1_or_text.setObjectName("w1_or_text")
        self.w1_tag = QtWidgets.QLabel(self.w1_tab1)
        self.w1_tag.setGeometry(QtCore.QRect(10, 80, 41, 31))
        self.w1_tag.setStyleSheet("color:#bad3e0")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_tag.setFont(font)
        self.w1_tag.setObjectName("w1_tag")
        self.w1_tag_text = QtWidgets.QLabel(self.w1_tab1)
        self.w1_tag_text.setGeometry(QtCore.QRect(50, 80, 611, 31))
        self.w1_tag_text.setStyleSheet("color:#66c0f4")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_tag_text.setFont(font)
        self.w1_tag_text.setObjectName("w1_tag_text")
        self.w1_price = QtWidgets.QLabel(self.w1_tab1)
        self.w1_price.setGeometry(QtCore.QRect(710, 40, 91, 41))

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.w1_price.setFont(font)
        self.w1_price.setObjectName("w1_price")
        self.w1_price.setStyleSheet("color:#809996")
        self.w1_tabWidget.addTab(self.w1_tab1, "")
        self.w1_tab2 = QtWidgets.QWidget()
        self.w1_tab2.setObjectName("w1_tab2")
        self.w1_dev = QtWidgets.QLabel(self.w1_tab2)
        self.w1_dev.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.w1_dev.setStyleSheet("color:#bad3e0")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_dev.setFont(font)
        self.w1_dev.setObjectName("w1_dev")
        self.w1_dev_text = QtWidgets.QLabel(self.w1_tab2)
        self.w1_dev_text.setGeometry(QtCore.QRect(70, 0, 551, 31))
        self.w1_dev_text.setStyleSheet("color:#66c0f4")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_dev_text.setFont(font)
        self.w1_dev_text.setObjectName("w1_dev_text")
        self.w1_ds = QtWidgets.QLabel(self.w1_tab2)
        self.w1_ds.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.w1_ds.setStyleSheet("color:#bad3e0")

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_ds.setFont(font)
        self.w1_ds.setObjectName("w1_ds")
        self.w1_ds_text = QtWidgets.QLabel(self.w1_tab2)
        self.w1_ds_text.setGeometry(QtCore.QRect(70, 40, 741, 81))
        self.w1_ds_text.setStyleSheet("color:#66c0f4")

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w1_ds_text.sizePolicy().hasHeightForWidth())
        self.w1_ds_text.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w1_ds_text.setFont(font)
        self.w1_ds_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w1_ds_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.w1_ds_text.setAcceptDrops(False)
        self.w1_ds_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w1_ds_text.setAutoFillBackground(False)
        self.w1_ds_text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.w1_ds_text.setObjectName("w1_ds_text")
        self.w1_tabWidget.addTab(self.w1_tab2, "")
        self.w1_img = QtWidgets.QLabel(self.w1)
        self.w1_img.setGeometry(QtCore.QRect(8, 8, 310, 145))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.w1_img.setFont(font)
        self.w1_img.setAlignment(QtCore.Qt.AlignCenter)
        self.w1_img.setObjectName("w1_img")
        self.w1_img.setStyleSheet("color:#495976;background:#313e54;border-radius:10px")

        self.w2 = QtWidgets.QWidget(self.centralwidget)
        self.w2.setGeometry(QtCore.QRect(270, 265, 1157, 161))
        self.w2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w2.setObjectName("w2")
        self.w2.setStyleSheet("background-color:#263550;border-radius:15px")
        self.w2_tabWidget = QtWidgets.QTabWidget(self.w2)
        self.w2_tabWidget.setGeometry(QtCore.QRect(330, 10, 821, 140))
        self.w2_tabWidget.setStyleSheet("color:#bad3e0")
        self.w2_tabWidget.setObjectName("w2_tabWidget")
        self.w2_tabWidget.setStyleSheet(
            "QTabWidget::pane{border-width:1px;border-color:rgb(255, 255, 255，160);background: transparent}"
            "QTabBar::tab{min-width:75px; min-height:22px;}"
            "QTabBar::tab:first:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:15;margin-right:2;}"
            "QTabBar::tab:first:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:first:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:last:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}")
        self.w2_tab1 = QtWidgets.QWidget()
        self.w2_tab1.setObjectName("w2_tab1")
        self.w2_tab1.setStyleSheet("background-color:#1c263a")
        self.w2_tab1.setStyleSheet("color:white")
        self.w2_name = QtWidgets.QLabel(self.w2_tab1)
        self.w2_name.setGeometry(QtCore.QRect(10, 10, 641, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.w2_name.setFont(font)
        self.w2_name.setObjectName("w2_name")
        self.w2_name.setStyleSheet("color:#bad3e0")
        self.w2_rr = QtWidgets.QLabel(self.w2_tab1)
        self.w2_rr.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_rr.setFont(font)
        self.w2_rr.setObjectName("w2_rr")
        self.w2_rr_text = QtWidgets.QLabel(self.w2_tab1)
        self.w2_rr_text.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.w2_rr.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_rr_text.setFont(font)
        self.w2_rr_text.setObjectName("w2_rr_text")
        self.w2_rr_text.setStyleSheet("color:#66c0f4")
        self.w2_or = QtWidgets.QLabel(self.w2_tab1)
        self.w2_or.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.w2_or.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_or.setFont(font)
        self.w2_or.setObjectName("w2_or")
        self.w2_or_text = QtWidgets.QLabel(self.w2_tab1)
        self.w2_or_text.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.w2_or_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_or_text.setFont(font)
        self.w2_or_text.setObjectName("w2_or_text")
        self.w2_tag = QtWidgets.QLabel(self.w2_tab1)
        self.w2_tag.setGeometry(QtCore.QRect(10, 80, 41, 31))
        self.w2_tag.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_tag.setFont(font)
        self.w2_tag.setObjectName("w2_tag")
        self.w2_tag_text = QtWidgets.QLabel(self.w2_tab1)
        self.w2_tag_text.setGeometry(QtCore.QRect(50, 80, 611, 31))
        self.w2_tag_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_tag_text.setFont(font)
        self.w2_tag_text.setObjectName("w2_tag_text")
        self.w2_price = QtWidgets.QLabel(self.w2_tab1)
        self.w2_price.setGeometry(QtCore.QRect(710, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.w2_price.setFont(font)
        self.w2_price.setObjectName("w2_price")
        self.w2_price.setStyleSheet("color:#809996")
        self.w2_tabWidget.addTab(self.w2_tab1, "")
        self.w2_tab2 = QtWidgets.QWidget()
        self.w2_tab2.setObjectName("w2_tab2")
        self.w2_dev = QtWidgets.QLabel(self.w2_tab2)
        self.w2_dev.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.w2_dev.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_dev.setFont(font)
        self.w2_dev.setObjectName("w2_dev")
        self.w2_dev_text = QtWidgets.QLabel(self.w2_tab2)
        self.w2_dev_text.setGeometry(QtCore.QRect(70, 0, 551, 31))
        self.w2_dev_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_dev_text.setFont(font)
        self.w2_dev_text.setObjectName("w2_dev_text")
        self.w2_ds = QtWidgets.QLabel(self.w2_tab2)
        self.w2_ds.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.w2_ds.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_ds.setFont(font)
        self.w2_ds.setObjectName("w2_ds")
        self.w2_ds_text = QtWidgets.QLabel(self.w2_tab2)
        self.w2_ds_text.setGeometry(QtCore.QRect(70, 40, 741, 81))
        self.w2_ds_text.setStyleSheet("color:#66c0f4")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w2_ds_text.sizePolicy().hasHeightForWidth())
        self.w2_ds_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w2_ds_text.setFont(font)
        self.w2_ds_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w2_ds_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.w2_ds_text.setAcceptDrops(False)
        self.w2_ds_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w2_ds_text.setAutoFillBackground(False)
        self.w2_ds_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.w2_ds_text.setObjectName("w2_ds_text")
        self.w2_tabWidget.addTab(self.w2_tab2, "")
        self.w2_img = QtWidgets.QLabel(self.w2)
        self.w2_img.setGeometry(QtCore.QRect(8, 8, 310, 145))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.w2_img.setFont(font)
        self.w2_img.setAlignment(QtCore.Qt.AlignCenter)
        self.w2_img.setObjectName("w2_img")
        self.w2_img.setStyleSheet("color:#495976;background:#313e54;border-radius:10px")

        self.w3 = QtWidgets.QWidget(self.centralwidget)
        self.w3.setGeometry(QtCore.QRect(270, 442, 1157, 161))
        self.w3.setObjectName("w3")
        self.w3.setStyleSheet("background-color:#263550;border-radius:15px")
        self.w3_tabWidget = QtWidgets.QTabWidget(self.w3)
        self.w3_tabWidget.setGeometry(QtCore.QRect(330, 10, 821, 140))
        self.w3_tabWidget.setStyleSheet("color:#bad3e0")
        self.w3_tabWidget.setObjectName("w3_tabWidget")
        self.w3_tabWidget.setStyleSheet(
            "QTabWidget::pane{border-width:1px;border-color:rgb(255, 255, 255，160);background: transparent}"
            "QTabBar::tab{min-width:75px; min-height:22px;}"
            "QTabBar::tab:first:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:15;margin-right:2;}"
            "QTabBar::tab:first:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:first:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:last:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}")
        self.w3_tab1 = QtWidgets.QWidget()
        self.w3_tab1.setObjectName("w3_tab1")
        self.w3_tab1.setStyleSheet("background-color:#1c263a")
        self.w3_tab1.setStyleSheet("color:white")
        self.w3_name = QtWidgets.QLabel(self.w3_tab1)
        self.w3_name.setGeometry(QtCore.QRect(10, 10, 641, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.w3_name.setFont(font)
        self.w3_name.setObjectName("w3_name")
        self.w3_name.setStyleSheet("color:#bad3e0")
        self.w3_rr = QtWidgets.QLabel(self.w3_tab1)
        self.w3_rr.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_rr.setFont(font)
        self.w3_rr.setObjectName("w3_rr")
        self.w3_rr_text = QtWidgets.QLabel(self.w3_tab1)
        self.w3_rr_text.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.w3_rr.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_rr_text.setFont(font)
        self.w3_rr_text.setObjectName("w3_rr_text")
        self.w3_rr_text.setStyleSheet("color:#66c0f4")
        self.w3_or = QtWidgets.QLabel(self.w3_tab1)
        self.w3_or.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.w3_or.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_or.setFont(font)
        self.w3_or.setObjectName("w3_or")
        self.w3_or_text = QtWidgets.QLabel(self.w3_tab1)
        self.w3_or_text.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.w3_or_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_or_text.setFont(font)
        self.w3_or_text.setObjectName("w3_or_text")
        self.w3_tag = QtWidgets.QLabel(self.w3_tab1)
        self.w3_tag.setGeometry(QtCore.QRect(10, 80, 41, 31))
        self.w3_tag.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_tag.setFont(font)
        self.w3_tag.setObjectName("w3_tag")
        self.w3_tag_text = QtWidgets.QLabel(self.w3_tab1)
        self.w3_tag_text.setGeometry(QtCore.QRect(50, 80, 611, 31))
        self.w3_tag_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_tag_text.setFont(font)
        self.w3_tag_text.setObjectName("w3_tag_text")
        self.w3_price = QtWidgets.QLabel(self.w3_tab1)
        self.w3_price.setGeometry(QtCore.QRect(710, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.w3_price.setFont(font)
        self.w3_price.setObjectName("w3_price")
        self.w3_price.setStyleSheet("color:#809996")
        self.w3_tabWidget.addTab(self.w3_tab1, "")
        self.w3_tab2 = QtWidgets.QWidget()
        self.w3_tab2.setObjectName("w3_tab2")
        self.w3_dev = QtWidgets.QLabel(self.w3_tab2)
        self.w3_dev.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.w3_dev.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_dev.setFont(font)
        self.w3_dev.setObjectName("w3_dev")
        self.w3_dev_text = QtWidgets.QLabel(self.w3_tab2)
        self.w3_dev_text.setGeometry(QtCore.QRect(70, 0, 551, 31))
        self.w3_dev_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_dev_text.setFont(font)
        self.w3_dev_text.setObjectName("w3_dev_text")
        self.w3_ds = QtWidgets.QLabel(self.w3_tab2)
        self.w3_ds.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.w3_ds.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_ds.setFont(font)
        self.w3_ds.setObjectName("w3_ds")
        self.w3_ds_text = QtWidgets.QLabel(self.w3_tab2)
        self.w3_ds_text.setGeometry(QtCore.QRect(70, 40, 741, 81))
        self.w3_ds_text.setStyleSheet("color:#66c0f4")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w3_ds_text.sizePolicy().hasHeightForWidth())
        self.w3_ds_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w3_ds_text.setFont(font)
        self.w3_ds_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w3_ds_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.w3_ds_text.setAcceptDrops(False)
        self.w3_ds_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w3_ds_text.setAutoFillBackground(False)
        self.w3_ds_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.w3_ds_text.setObjectName("w3_ds_text")
        self.w3_tabWidget.addTab(self.w3_tab2, "")
        self.w3_img = QtWidgets.QLabel(self.w3)
        self.w3_img.setGeometry(QtCore.QRect(8, 8, 310, 145))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.w3_img.setFont(font)
        self.w3_img.setAlignment(QtCore.Qt.AlignCenter)
        self.w3_img.setObjectName("w3_img")
        self.w3_img.setStyleSheet("color:#495976;background:#313e54;border-radius:10px")

        self.w4 = QtWidgets.QWidget(self.centralwidget)
        self.w4.setGeometry(QtCore.QRect(270, 619, 1157, 161))
        self.w4.setObjectName("w4")
        self.w4.setStyleSheet("background-color:#263550;border-radius:15px")
        self.w4_tabWidget = QtWidgets.QTabWidget(self.w4)
        self.w4_tabWidget.setGeometry(QtCore.QRect(330, 10, 821, 140))
        self.w4_tabWidget.setStyleSheet("color:#bad3e0")
        self.w4_tabWidget.setObjectName("w4_tabWidget")
        self.w4_tabWidget.setStyleSheet(
            "QTabWidget::pane{border-width:1px;border-color:rgb(255, 255, 255，160);background: transparent}"
            "QTabBar::tab{min-width:75px; min-height:22px;}"
            "QTabBar::tab:first:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:15;margin-right:2;}"
            "QTabBar::tab:first:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:first:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:last:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}")
        self.w4_tab1 = QtWidgets.QWidget()
        self.w4_tab1.setObjectName("w4_tab1")
        self.w4_tab1.setStyleSheet("background-color:#1c263a")
        self.w4_tab1.setStyleSheet("color:white")
        self.w4_name = QtWidgets.QLabel(self.w4_tab1)
        self.w4_name.setGeometry(QtCore.QRect(10, 10, 641, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.w4_name.setFont(font)
        self.w4_name.setObjectName("w4_name")
        self.w4_name.setStyleSheet("color:#bad3e0")
        self.w4_rr = QtWidgets.QLabel(self.w4_tab1)
        self.w4_rr.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_rr.setFont(font)
        self.w4_rr.setObjectName("w4_rr")
        self.w4_rr_text = QtWidgets.QLabel(self.w4_tab1)
        self.w4_rr_text.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.w4_rr.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_rr_text.setFont(font)
        self.w4_rr_text.setObjectName("w4_rr_text")
        self.w4_rr_text.setStyleSheet("color:#66c0f4")
        self.w4_or = QtWidgets.QLabel(self.w4_tab1)
        self.w4_or.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.w4_or.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_or.setFont(font)
        self.w4_or.setObjectName("w4_or")
        self.w4_or_text = QtWidgets.QLabel(self.w4_tab1)
        self.w4_or_text.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.w4_or_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_or_text.setFont(font)
        self.w4_or_text.setObjectName("w4_or_text")
        self.w4_tag = QtWidgets.QLabel(self.w4_tab1)
        self.w4_tag.setGeometry(QtCore.QRect(10, 80, 41, 31))
        self.w4_tag.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_tag.setFont(font)
        self.w4_tag.setObjectName("w4_tag")
        self.w4_tag_text = QtWidgets.QLabel(self.w4_tab1)
        self.w4_tag_text.setGeometry(QtCore.QRect(50, 80, 611, 31))
        self.w4_tag_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_tag_text.setFont(font)
        self.w4_tag_text.setObjectName("w4_tag_text")
        self.w4_price = QtWidgets.QLabel(self.w4_tab1)
        self.w4_price.setGeometry(QtCore.QRect(710, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.w4_price.setFont(font)
        self.w4_price.setObjectName("w4_price")
        self.w4_price.setStyleSheet("color:#809996")
        self.w4_tabWidget.addTab(self.w4_tab1, "")
        self.w4_tab2 = QtWidgets.QWidget()
        self.w4_tab2.setObjectName("w4_tab2")
        self.w4_dev = QtWidgets.QLabel(self.w4_tab2)
        self.w4_dev.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.w4_dev.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_dev.setFont(font)
        self.w4_dev.setObjectName("w4_dev")
        self.w4_dev_text = QtWidgets.QLabel(self.w4_tab2)
        self.w4_dev_text.setGeometry(QtCore.QRect(70, 0, 551, 31))
        self.w4_dev_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_dev_text.setFont(font)
        self.w4_dev_text.setObjectName("w4_dev_text")
        self.w4_ds = QtWidgets.QLabel(self.w4_tab2)
        self.w4_ds.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.w4_ds.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_ds.setFont(font)
        self.w4_ds.setObjectName("w4_ds")
        self.w4_ds_text = QtWidgets.QLabel(self.w4_tab2)
        self.w4_ds_text.setGeometry(QtCore.QRect(70, 40, 741, 81))
        self.w4_ds_text.setStyleSheet("color:#66c0f4")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w4_ds_text.sizePolicy().hasHeightForWidth())
        self.w4_ds_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w4_ds_text.setFont(font)
        self.w4_ds_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w4_ds_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.w4_ds_text.setAcceptDrops(False)
        self.w4_ds_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w4_ds_text.setAutoFillBackground(False)
        self.w4_ds_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.w4_ds_text.setObjectName("w4_ds_text")
        self.w4_tabWidget.addTab(self.w4_tab2, "")
        self.w4_img = QtWidgets.QLabel(self.w4)
        self.w4_img.setGeometry(QtCore.QRect(8, 8, 310, 145))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.w4_img.setFont(font)
        self.w4_img.setAlignment(QtCore.Qt.AlignCenter)
        self.w4_img.setObjectName("w4_img")
        self.w4_img.setStyleSheet("color:#495976;background:#313e54;border-radius:10px")

        self.w5 = QtWidgets.QWidget(self.centralwidget)
        self.w5.setGeometry(QtCore.QRect(270, 796, 1157, 161))
        self.w5.setObjectName("w5")
        self.w5.setStyleSheet("background-color:#263550;border-radius:15px")
        self.w5_tabWidget = QtWidgets.QTabWidget(self.w5)
        self.w5_tabWidget.setGeometry(QtCore.QRect(330, 10, 821, 140))
        self.w5_tabWidget.setStyleSheet("color:#bad3e0")
        self.w5_tabWidget.setObjectName("w5_tabWidget")
        self.w5_tabWidget.setStyleSheet(
            "QTabWidget::pane{border-width:1px;border-color:rgb(255, 255, 255，160);background: transparent}"
            "QTabBar::tab{min-width:75px; min-height:22px;}"
            "QTabBar::tab:first:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:15;margin-right:2;}"
            "QTabBar::tab:first:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:first:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:15;margin-right:2}"
            "QTabBar::tab:last:selected{color:white;background:#495976;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:!selected{color:white;background:#313e54;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}"
            "QTabBar::tab:last:hover:!selected{color:white;background:#667288;border-radius:2px;margin-top:0;margin-left:0;margin-right:2}")
        self.w5_tab1 = QtWidgets.QWidget()
        self.w5_tab1.setObjectName("w5_tab1")
        self.w5_tab1.setStyleSheet("background-color:#1c263a")
        self.w5_tab1.setStyleSheet("color:white")
        self.w5_name = QtWidgets.QLabel(self.w5_tab1)
        self.w5_name.setGeometry(QtCore.QRect(10, 10, 641, 40))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.w5_name.setFont(font)
        self.w5_name.setObjectName("w5_name")
        self.w5_name.setStyleSheet("color:#bad3e0")
        self.w5_rr = QtWidgets.QLabel(self.w5_tab1)
        self.w5_rr.setGeometry(QtCore.QRect(10, 50, 71, 31))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_rr.setFont(font)
        self.w5_rr.setObjectName("w5_rr")
        self.w5_rr_text = QtWidgets.QLabel(self.w5_tab1)
        self.w5_rr_text.setGeometry(QtCore.QRect(80, 50, 71, 31))
        self.w5_rr.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_rr_text.setFont(font)
        self.w5_rr_text.setObjectName("w5_rr_text")
        self.w5_rr_text.setStyleSheet("color:#66c0f4")
        self.w5_or = QtWidgets.QLabel(self.w5_tab1)
        self.w5_or.setGeometry(QtCore.QRect(160, 50, 71, 31))
        self.w5_or.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_or.setFont(font)
        self.w5_or.setObjectName("w5_or")
        self.w5_or_text = QtWidgets.QLabel(self.w5_tab1)
        self.w5_or_text.setGeometry(QtCore.QRect(230, 50, 71, 31))
        self.w5_or_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_or_text.setFont(font)
        self.w5_or_text.setObjectName("w5_or_text")
        self.w5_tag = QtWidgets.QLabel(self.w5_tab1)
        self.w5_tag.setGeometry(QtCore.QRect(10, 80, 41, 31))
        self.w5_tag.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_tag.setFont(font)
        self.w5_tag.setObjectName("w5_tag")
        self.w5_tag_text = QtWidgets.QLabel(self.w5_tab1)
        self.w5_tag_text.setGeometry(QtCore.QRect(50, 80, 611, 31))
        self.w5_tag_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_tag_text.setFont(font)
        self.w5_tag_text.setObjectName("w5_tag_text")
        self.w5_price = QtWidgets.QLabel(self.w5_tab1)
        self.w5_price.setGeometry(QtCore.QRect(710, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(23)
        font.setBold(True)
        font.setWeight(75)
        self.w5_price.setFont(font)
        self.w5_price.setObjectName("w5_price")
        self.w5_price.setStyleSheet("color:#809996")
        self.w5_tabWidget.addTab(self.w5_tab1, "")
        self.w5_tab2 = QtWidgets.QWidget()
        self.w5_tab2.setObjectName("w5_tab2")
        self.w5_dev = QtWidgets.QLabel(self.w5_tab2)
        self.w5_dev.setGeometry(QtCore.QRect(10, 0, 51, 31))
        self.w5_dev.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_dev.setFont(font)
        self.w5_dev.setObjectName("w5_dev")
        self.w5_dev_text = QtWidgets.QLabel(self.w5_tab2)
        self.w5_dev_text.setGeometry(QtCore.QRect(70, 0, 551, 31))
        self.w5_dev_text.setStyleSheet("color:#66c0f4")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_dev_text.setFont(font)
        self.w5_dev_text.setObjectName("w5_dev_text")
        self.w5_ds = QtWidgets.QLabel(self.w5_tab2)
        self.w5_ds.setGeometry(QtCore.QRect(10, 30, 51, 31))
        self.w5_ds.setStyleSheet("color:#bad3e0")
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_ds.setFont(font)
        self.w5_ds.setObjectName("w5_ds")
        self.w5_ds_text = QtWidgets.QLabel(self.w5_tab2)
        self.w5_ds_text.setGeometry(QtCore.QRect(70, 40, 741, 81))
        self.w5_ds_text.setStyleSheet("color:#66c0f4")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.w5_ds_text.sizePolicy().hasHeightForWidth())
        self.w5_ds_text.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(11)
        self.w5_ds_text.setFont(font)
        self.w5_ds_text.setFocusPolicy(QtCore.Qt.NoFocus)
        self.w5_ds_text.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.w5_ds_text.setAcceptDrops(False)
        self.w5_ds_text.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.w5_ds_text.setAutoFillBackground(False)
        self.w5_ds_text.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.w5_ds_text.setObjectName("w5_ds_text")
        self.w5_tabWidget.addTab(self.w5_tab2, "")
        self.w5_img = QtWidgets.QLabel(self.w5)
        self.w5_img.setGeometry(QtCore.QRect(8, 8, 310, 145))
        font = QtGui.QFont()
        font.setFamily("等线")
        font.setPointSize(100)
        font.setBold(True)
        font.setWeight(75)
        self.w5_img.setFont(font)
        self.w5_img.setAlignment(QtCore.Qt.AlignCenter)
        self.w5_img.setObjectName("w5_img")
        self.w5_img.setStyleSheet("color:#495976;background:#313e54;border-radius:10px")

        self.w1_ds_text.setWordWrap(True)
        self.w2_ds_text.setWordWrap(True)
        self.w3_ds_text.setWordWrap(True)
        self.w4_ds_text.setWordWrap(True)
        self.w5_ds_text.setWordWrap(True)


        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(13, 5, 191, 21))

        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet("color:white")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.w1_tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.w1_name.setText(_translate("MainWindow", "Game Name"))
        self.w1_rr.setText(_translate("MainWindow", "最近评价："))
        self.w1_rr_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w1_or.setText(_translate("MainWindow", "总体评价："))
        self.w1_or_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w1_tag.setText(_translate("MainWindow", "标签："))
        self.w1_tag_text.setText(_translate("MainWindow", "TAG1  TAG2  TAG3  TAG4  TAG5  ......"))
        self.w1_price.setText(_translate("MainWindow", "¥ 233"))
        self.w1_tabWidget.setTabText(self.w1_tabWidget.indexOf(self.w1_tab1), _translate("MainWindow", "简述"))
        self.w1_dev.setText(_translate("MainWindow", "开发者："))
        self.w1_dev_text.setText(_translate("MainWindow", "UNKNOW COMPANY"))
        self.w1_ds.setText(_translate("MainWindow", "简    介："))
        self.w1_ds_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w1_tabWidget.setTabText(self.w1_tabWidget.indexOf(self.w1_tab2), _translate("MainWindow", "详情"))
        self.w1_img.setText(_translate("MainWindow", "IMG"))
        self.w2_name.setText(_translate("MainWindow", "Game Name"))
        self.w2_rr.setText(_translate("MainWindow", "最近评价："))
        self.w2_rr_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w2_or.setText(_translate("MainWindow", "总体评价："))
        self.w2_or_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w2_tag.setText(_translate("MainWindow", "标签："))
        self.w2_tag_text.setText(_translate("MainWindow", "TAG1  TAG2  TAG3  TAG4  TAG5  ......"))
        self.w2_price.setText(_translate("MainWindow", "¥ 233"))
        self.w2_tabWidget.setTabText(self.w2_tabWidget.indexOf(self.w2_tab1), _translate("MainWindow", "简述"))
        self.w2_dev.setText(_translate("MainWindow", "开发者："))
        self.w2_dev_text.setText(_translate("MainWindow", "UNKNOW COMPANY"))
        self.w2_ds.setText(_translate("MainWindow", "简    介："))
        self.w2_ds_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w2_tabWidget.setTabText(self.w2_tabWidget.indexOf(self.w2_tab2), _translate("MainWindow", "详情"))
        self.w2_img.setText(_translate("MainWindow", "IMG"))
        self.w3_name.setText(_translate("MainWindow", "Game Name"))
        self.w3_rr.setText(_translate("MainWindow", "最近评价："))
        self.w3_rr_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w3_or.setText(_translate("MainWindow", "总体评价："))
        self.w3_or_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w3_tag.setText(_translate("MainWindow", "标签："))
        self.w3_tag_text.setText(_translate("MainWindow", "TAG1  TAG2  TAG3  TAG4  TAG5  ......"))
        self.w3_price.setText(_translate("MainWindow", "¥ 233"))
        self.w3_tabWidget.setTabText(self.w3_tabWidget.indexOf(self.w3_tab1), _translate("MainWindow", "简述"))
        self.w3_dev.setText(_translate("MainWindow", "开发者："))
        self.w3_dev_text.setText(_translate("MainWindow", "UNKNOW COMPANY"))
        self.w3_ds.setText(_translate("MainWindow", "简    介："))
        self.w3_ds_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w3_tabWidget.setTabText(self.w3_tabWidget.indexOf(self.w3_tab2), _translate("MainWindow", "详情"))
        self.w3_img.setText(_translate("MainWindow", "IMG"))
        self.w4_name.setText(_translate("MainWindow", "Game Name"))
        self.w4_rr.setText(_translate("MainWindow", "最近评价："))
        self.w4_rr_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w4_or.setText(_translate("MainWindow", "总体评价："))
        self.w4_or_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w4_tag.setText(_translate("MainWindow", "标签："))
        self.w4_tag_text.setText(_translate("MainWindow", "TAG1  TAG2  TAG3  TAG4  TAG5  ......"))
        self.w4_price.setText(_translate("MainWindow", "¥ 233"))
        self.w4_tabWidget.setTabText(self.w4_tabWidget.indexOf(self.w4_tab1), _translate("MainWindow", "简述"))
        self.w4_dev.setText(_translate("MainWindow", "开发者："))
        self.w4_dev_text.setText(_translate("MainWindow", "UNKNOW COMPANY"))
        self.w4_ds.setText(_translate("MainWindow", "简    介："))
        self.w4_ds_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w4_tabWidget.setTabText(self.w4_tabWidget.indexOf(self.w4_tab2), _translate("MainWindow", "详情"))
        self.w4_img.setText(_translate("MainWindow", "IMG"))
        self.w5_name.setText(_translate("MainWindow", "Game Name"))
        self.w5_rr.setText(_translate("MainWindow", "最近评价："))
        self.w5_rr_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w5_or.setText(_translate("MainWindow", "总体评价："))
        self.w5_or_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w5_tag.setText(_translate("MainWindow", "标签："))
        self.w5_tag_text.setText(_translate("MainWindow", "TAG1  TAG2  TAG3  TAG4  TAG5  ......"))
        self.w5_price.setText(_translate("MainWindow", "¥ 233"))
        self.w5_tabWidget.setTabText(self.w5_tabWidget.indexOf(self.w5_tab1), _translate("MainWindow", "简述"))
        self.w5_dev.setText(_translate("MainWindow", "开发者："))
        self.w5_dev_text.setText(_translate("MainWindow", "UNKNOW COMPANY"))
        self.w5_ds.setText(_translate("MainWindow", "简    介："))
        self.w5_ds_text.setText(_translate("MainWindow", "UNKNOW"))
        self.w5_tabWidget.setTabText(self.w5_tabWidget.indexOf(self.w5_tab2), _translate("MainWindow", "详情"))
        self.w5_img.setText(_translate("MainWindow", "IMG"))
        self.label_2.setText(_translate("MainWindow", "Steam推荐 - Tags Choose"))
