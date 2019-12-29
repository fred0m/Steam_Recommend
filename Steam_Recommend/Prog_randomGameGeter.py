import random
import pandas as pd
class randomGameGeter:
    def __init__(self):
        self.raw_data = pd.read_csv("Data_GameList.csv").values.tolist()
        self.rlist = random.sample(range(0,781),11)

    def get(self):
        re = []
        for i in self.rlist:
            re.append(self.raw_data[i][0])
        return re

    def reflash(self):
        self.rlist = random.sample(range(0,781),11)

if __name__ == "__main__":
    demo = randomGameGeter()
    print(demo.get())
    demo.reflash()
    print(demo.get())
    demo.reflash()
    print(demo.get())
    demo.reflash()
    print(demo.get())
    demo.reflash()
    print(demo.get())
