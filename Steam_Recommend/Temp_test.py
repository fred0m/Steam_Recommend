lst_game = []
#temp_dict = dict([('Gamename','ERROR: Getting Game Failed'),('Developer','Plaese choose your game again','Recent Reviews'),('Recent Reviews','Unknow'),('Overall Reviews','Unknow'),('Description','Unknow'),('Price','Unknow'),('Tag','Unknow')])
temp_dict = {'Gamename': 'ERROR: Getting Game Failed', 'Developer': 'Plaese choose your game again','Recent Reviews': 'Unknow', 'Overall Reviews': 'Unknow', 'Description': 'Unknow','Price': 'Unknow', 'Tag': 'Unknow'}
for j in range(3):
    lst_game.append(temp_dict)
print(lst_game)
for i in range(3):
    print(type(lst_game[i]))