import requests
from bs4 import BeautifulSoup
from Es import WebGeter
import os

class imgGeter:
    def __init__(self,url):
        self.url = url
        self.raw_data = WebGeter(self.url)
        self.raw_data = self.raw_data.raw_data

    def getHeaderImg(self):
        re = self.raw_data.find(name="img",attrs={"class":"game_header_image_full"}).get("src")
        return re

    def getImgList(self):#返回值为二重列表[[],[]]第一个列表为小图，第二个为大图                                                      # highlight_screenshot_link  highlight_strip
        big = []
        small = []
        t = self.raw_data.find(id="highlight_player_area").findAll(name="a",attrs={"class":"highlight_screenshot_link"})
        for i in t:
            big.append(i.get("href"))
        t2 = self.raw_data.find(id="highlight_strip").findAll(name="div",attrs={"class":"highlight_strip_item highlight_strip_screenshot"})
        for i in t2:
            small.append(i.find(name="img").get("src"))
        return [small,big]

    def saveImg(self,url,filename):
        file = requests.get(url)
        if file.status_code == 200:
            with open(filename+".jpg","wb") as f:
                f.write(file.content)

if __name__ == '__main__':
    a =imgGeter("https://store.steampowered.com/app/851100/?curator_clanid=32686107")
    a.saveImg(a.getHeaderImg(),"logo5")
