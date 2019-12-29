#encoding=utf-8
import sys
import os
import time
import Es
import re
import linecache
import numpy
import Prog_imgGeter




def cls():
    os.system('cls')

personData = []


def sprint(string,t=0.5): #debug阶段t=0 正式阶段t=1/t=0.5
    print(string)
    time.sleep(t)

def load():
    filename = "Data_TagRequestList.data"
    data = {}
    f = open(filename,'r',encoding='utf-8')

    for i in range(0,266,2):
        data[f.readline().strip('\n')] = f.readline().strip('\n')

    data.items()#字典键值对反转
    zip(data.values(),data.keys())
    data = dict(zip(data.values(),data.keys()))

    f.close()
    return data

data = load()
'''
for i in range(0,250):
    os.system("python moreInfo.py "+data[i][1])
    #print (data[i][3])
    time.sleep(10)
'''

def welcome():
    sprint("ascii 字符画")
    sprint("欢迎使用#steam游戏推荐程序")
    sprint("后期慢慢完善",2)


def changedata():
    check = False
    sprint("当前你已经选择的类型为")
    sprint(personData)
    sprint("你希望进行哪种操作？")
    sprint("1.添加类型")
    sprint("2.删除类型")
    sprint("3.下一步")
    way = input(">")
    if(way=="1"):
        #for typename in data:
            #sprint(typename,0)
        sprint("请输入上述出现过的类型名，请保证与出现过的类型名一致")
        temp = input(">").replace(" ","")
        for i in data:
            if (i==temp):
                check = True
        if (check):
            personData.append(temp)
            sprint("添加完成")
        else:
            sprint("请检查拼写是否出错哦")
        cls()
        changedata()
    elif(way=="2"):
        sprint(personData)
        sprint("请输入你已经选择的类型名，请保证与上方括号内已有的类型名一致")
        temp = input(">").replace(" ","").replace(",","")
        for i in personData:
            if (i==temp):
                check = True
        if (check):
            personData.remove(temp)
            sprint("删除完成")
        else:
            sprint("请检查拼写是否出错哦")
        cls()
        changedata()
    elif(way=="3"):
        infoAnalysis()
    else:
        sprint("请按提示输入哦")
        cls()
        changedata()

def typeTag():
    sprint("接下来会向你展示我们支持的类型")
    #for typename in data:
        #sprint(typename,0.05)#正式发布时请改为0.1
    changedata()

def wayToGetTag():
    sprint("你希望使用哪种方式进行推荐？")
    sprint("1.我知道我想要哪种游戏,我要自己指定类型")
    sprint("2.我也不知道我想要哪种游戏")
    way = input(">")
    if(way=="1"):
        typeTag()
    elif(way=='2'):
        anotherTag()
    else:
        sprint("请按提示输入哦")
        cls()
        wayToGetTag()


def infoAnalysis(we):
    lst_demo = []
    print("您选择了 \""+we+"\" 标签，正在为您获取游戏信息...")
    fill="Data_TagRequestList.data"
    f = open(fill,'r',encoding='utf-8')
    line=f.readlines()
    errlist = []
    for i in range(0,266):
        if line[i].strip('\n')==we:   #定位
            l=i
            kk=linecache.getline("Data_TagRequestList.data", l+2).strip('\n')#获取网址
            demo = Es.WebGeter(kk)
            demodata = Es.steam250URLGeter(demo.raw_data)#输入解析后的网页
            demodata.dataHandle()#使用数据解析方法
############################代码修改#################################
            n = 50 #输出前五
            num = 0
            for k in range(0,n):#输出前五
                try:
                    t=demodata.data[k][1]
                    demo = Es.detailsDataGeter(t)
                    demo.detailsGeterFixed()#需要执行此方法才能开始解析

                    temp_img = Prog_imgGeter.imgGeter(str(t))
                    temp_img.saveImg(temp_img.getHeaderImg(),"tag_logo"+str(num + 1))

                    print("游戏" + str(num + 1) + "信息获取成功")
                    lst_demo.append(demo.data)
                    num += 1
                except:
                    errlist.append(k)####记录出错的序号，调用时记得规避
                    n += 1
                    continue
                if(num==5):
                      break
    print("请浏览我们为您精选的游戏~~~~")
    return lst_demo

     #数据类型为列表格式为[游戏名,steam商店页面,评分]
###########################代码修改结束(he)############################
def anotherTag():
    print("正在为您获取top10游戏，请稍后...")
    lst_top = []
    errlist = []
############################代码修改#################################
    n = 50 #输出前十
    demo = Es.WebGeter("https://steam250.com/")
    demodata = Es.steam250URLGeter(demo.raw_data)#输入解析后的网页
    demodata.dataHandle()#使用数据解析方法
    num = 0
    for i in range(0,n):
        try:
            t=demodata.data[i][1]
            demo = Es.detailsDataGeter(t)
            demo.detailsGeterFixed()#需要执行此方法才能开始解析
            print("游戏"+str(num + 1)+"信息获取成功")
            lst_top.append(demo.data)#数据为字典类型
            temp_img = Prog_imgGeter.imgGeter(str(t))
            temp_img.saveImg(temp_img.getHeaderImg(), "top_logo" + str(num + 1))
            num += 1
        except:
            errlist.append(i)
            n += 1####记录出错的序号，调用时记得规避
            continue
        if(num==10):
            break
    return lst_top

###########################代码修改结束(he)############################


if __name__ == '__main__':
    wayToGetTag()

