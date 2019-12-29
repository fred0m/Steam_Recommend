import pandas as pd
import random
#-------------------------------#
'''
需要使用以下所有函数及变量
如三个游戏g1、g2、g3
'''

sourse_data = pd.read_csv("Data_Steam_User.csv")
#sourse_data = pd.read_csv("game_play.csv")
#sd = sourse_data.values.tolist()                                       #sourse_data列表
psd = sourse_data.values.tolist()
#print(sourse_data)
def sd_make(sd):
    num = 0
    s = []
    for it in sd:                                                      #num为非purchase部分
        if it[2] == 'purchase':
            num += 1
    for it in sd:
        if 'purchase' not in it:
            s.append(it)
    for i in range(len(s)):
        s[i].pop(2)
        s[i].pop(3)
    return s


def datamake(sd):
    sum = len(sd)                                                         #sd行数而非个数
    temp = sd[0][0]
    n = num = 1
    sdd = []
    data = []
    for i in range(sum):                                                    #用户总数
        if temp != sd[i][0]:
            num += 1
            temp = sd[i][0]                                                   #更新temp
    for i in range(sum):                                                    #将用户个数分序号并加入一个列表中作为头存在
        sdd.append([])
        sdd[i].append(i)
    n = 0
    for it in sd:                             #数据小没问题，至少每项的第一项都是相同的
        if temp == it[0]:
            sdd[n].append(it)
        else:
            n += 1
            temp = it[0]
            sdd[n].append(it)
    #上一层已经处理好
    #设置data
    #print(sdd)
    for items in sdd:
        if len(items)>1:
            data.append([])

    temp = sd[0][0]
    m = 0
    for items in sd:
        if items[0] == temp:
            data[m].append(items[1])
        else:
            m += 1
            data[m].append(items[1])
            temp = items[0]
            #data构建完毕但仍未满足需要，将data的数据按时间顺序进行排列
            #分析各个游戏在人群中的出现频率

    return data
    #return sd#data                       #总的data分布
def judge(data,g1,g2,g3):                         #判断游戏序列类型
    status = 0
    m = n = z = x = y = 0
    for i in range(len(data)):
        if g1 in data[i] and g2 in data[i] and g3 in data[i]:                    #只要这种情况存在就会使得三个同时存在的情况成立
            n += 1
        elif g1 in data[i] and g2 in data[i] and g3 not in data[i]:
            x += 1
        elif g1 in data[i] and g3 in data[i] and g2 not in data[i]:
            y += 1
        elif g2 in data[i] and g3 in data[i] and g1 not in data[i]:
            z += 1
    if n > 0:
        status = 1
        #print("三个都有")
    elif x > 0:
        status = 2
        #print("g1、g2")
    elif y > 0:
        status = 3
        #print("g1、g3")
    elif z > 0:
        status = 4
        #print("g2、g3")
    else:
        status = 0
        #print("一个都没有")
    return status

def search(data,g1,g2,g3,status):               #输入三个游戏g1、g2、g3
    node = []
    if status == 1:
        for i in range(len(data)):
            if g1 in data[i] and g2 in data[i] and g3 in data[i]:
                node.append(i)
    if status == 2:
        for i in range(len(data)):
            if g1 in data[i] and g2 in data[i]:
                node.append(i)
    if status == 3:
        for i in range(len(data)):
            if g1 in data[i] and g3 in data[i]:
                node.append(i)
    if status == 4:
        for i in range(len(data)):
            if g2 in data[i] and g3 in data[i]:
                node.append(i)
    return node
def remake(data,node):                #找出node中各个列表中重复的部分
    commons = []
    commons.append(data[node[0]][0])
    for iterms in node:                #data的栈数
        for iterm in data[iterms]:         #data【items】中的元素
            if iterm not in commons:
                commons.append(iterm)
    return commons
#暂定support值为1/4*m           m为人数，然后输出数据回到sd中
def m_datanum(data,g1,g2,g3,status):         #输入三个游戏g1、g2、g3
    member = 0
    if status == 1:
        for i in range(len(data)):
            if g1 in data[i] and g2 in data[i] and g3 in data[i]:
                member += 1
    if status == 2:
        for i in range(len(data)):
            if g1 in data[i] and g2 in data[i]:
                member += 1
    if status == 3:
        for i in range(len(data)):
            if g1 in data[i] and g3 in data[i]:
                member += 1
    if status == 4:
        for i in range(len(data)):
            if g2 in data[i] and g3 in data[i]:
                member += 1
    return member
def u_datanum(data,node,common):                 #每个相同游戏的量
    nn = []
    for it in common:                #若it在data[iterms]中
        n = 0
        for iterms in node:                #data的栈数
            if it in data[iterms]:
                n += 1
        nn.append(n)

    return nn
def g_datanum(data,node,common,g1,g2,g3,status):           #输入游戏的量
    nn = []
    n = 0
    if status == 1:
            for iterms in node:
                if g1 in data[iterms]:
                    n += 1
            nn.append(n)
            n = 0
            for iterms in node:
                if g2 in data[iterms]:
                    n += 1
            nn.append(n)
            n = 0
            for iterms in node:
                if g3 in data[iterms]:
                    n += 1
            nn.append(n)
    if status == 2:
            for iterms in node:
                if g1 in data[iterms]:
                    n += 1
            nn.append(n)
            n = 0
            for iterms in node:
                if g2 in data[iterms]:
                    n += 1
            nn.append(n)
    if status == 3:
            for iterms in node:
                if g1 in data[iterms]:
                    n += 1
            nn.append(n)
            n = 0
            for iterms in node:
                if g3 in data[iterms]:
                    n += 1
            nn.append(n)
    if status == 4:
            for iterms in node:
                if g2 in data[iterms]:
                    n += 1
            nn.append(n)
            n = 0
            for iterms in node:
                if g3 in data[iterms]:
                    n += 1
            nn.append(n)
    return nn

def offer(data,node,common,u_num,g_num,m_num,g1,g2,g3,status):
    game = []
    pg = []
    if status == 1:
        pg.append(g1)
        pg.append(g2)
        pg.append(g3)
        n = 0
        while n < 6:
            it = random.randint(0,len(common))
            rn = common[it]
            if rn not in pg and u_num[it] > int(1/4 * m_num ):
                n += 1
                game.append(rn)
    if status == 2:
        pg.append(g1)
        pg.append(g2)
        n = 0
        while n < 6:
            it = random.randint(0,len(common))
            rn = common[it]
            if rn not in pg and u_num[it] > int(1/4 * m_num ):
                n += 1
                game.append(rn)
    if status == 3:
        pg.append(g1)
        pg.append(g3)
        n = 0
        while n < 6:
            it = random.randint(0,len(common))
            rn = common[it]
            if rn not in pg and u_num[it] > int(1/4 * m_num ):
                n += 1
                game.append(rn)
    if status == 4:
        pg.append(g2)
        pg.append(g3)
        n = 0
        while n < 6:
            it = random.randint(0,len(common))
            rn = common[it]
            if rn not in pg and u_num[it] > int(1/4 * m_num ):
                n += 1
                game.append(rn)
    return game

def study(game,data,g1,g2,g3,status):                         #done
    new_game = []
    if status == 1:
        new_game.append(g1)
        new_game.append(g2)
        new_game.append(g3)
        for it in game:
            new_game.append(it)
            data.append([])
        for it in new_game:
            data[len(data)-1].append(it)
    if status == 2:
        new_game.append(g1)
        new_game.append(g2)
        for it in game:
            new_game.append(it)
            data.append([])
        for it in new_game:
            data[len(data)-1].append(it)
    if status == 3:
        new_game.append(g1)
        new_game.append(g3)
        for it in game:
            new_game.append(it)
            data.append([])
        for it in new_game:
            data[len(data)-1].append(it)
    if status == 4:
        new_game.append(g2)
        new_game.append(g3)
        for it in game:
            new_game.append(it)
            data.append([])
        for it in new_game:
            data[len(data)-1].append(it)
    if status == 5:
        data[len(data)-1].append(g1)
        data[len(data)-1].append(g2)
        data[len(data)-1].append(g3)
    return data

def GetGame(te_lst):
    sd = sd_make(psd)
    g1 = te_lst[0]
    g2 = te_lst[1]
    g3 = te_lst[2]
    data = datamake(sd)
    status = judge(data, g1, g2, g3)
    node = search(data, g1, g2, g3, status)
    common = remake(data, node)
    u_num = u_datanum(data, node, common)  # 只有common和u_num有一一对应关系
    g_num = g_datanum(data, node, common, g1, g2, g3, status)
    m_num = m_datanum(data, g1, g2, g3, status)
    game = offer(data, node, common, u_num, g_num, m_num, g1, g2, g3, status)
    return game

if __name__ == '__main__':
    lst = ['GRID Autosport', 'Time Clickers', 'Aliens Colonial Marines']
    print(GetGame(lst))