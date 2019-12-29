import Prog_randomGameGeter
import Prog_GameRecommend

demo = Prog_randomGameGeter.randomGameGeter()
lst1 = demo.get()

lst2 = []
for i in range(3):
    lst2.append(lst1[i])
print(lst2)
print(Prog_GameRecommend.GetGame(lst2))
