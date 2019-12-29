#encoding=utf-8
#---------------------------------------------------------------------------------------------------
#Copyright: Copyright (c) 2019
#Created on 2019-11-19
#Author: fredom
#Version 1.0.0
#---------------------------------------------------------------------------------------------------

import requests
from bs4 import BeautifulSoup
import Es
import os
import json
from urllib.parse import quote
steam_serch = "https://store.steampowered.com/search/?term="


class GetURLbyName :
    def __init__(self,name):
        self.name = name

    def __del__(self):
        pass

    def changeName(self,newname):
        self.name = newname

    def run(self):
        self.rawdata = Es.WebGeter(steam_serch+quote(self.name))
        self.url = self.rawdata.raw_data.find(name = "span",attrs = {"class":"title"}).parent.parent.parent.get('href')#定位URL默认返回第一个
        #self.appid = self.rawdata.raw_data.find(name = "span",attrs = {"class":"title"}).parent.parent.parent.get('data-ds-appid')
        #self.tagid = self.rawdata.raw_data.find(name = "span",attrs = {"class":"title"}).parent.parent.parent.get('data-ds-appid')
        #t = self.rawdata.raw_data.find(name = "span",attrs = {"class":"title"}).parent.parent.parent.get('data-ds-tagids')
        #t = t.replace('[','').replace(']','')
        #self.tagid = t.split(",")
        return self.url


class TagListGeter :
    def __init__ (self):
        self.url = "https://store.steampowered.com/tag/browse/#global_492"
        self.raw_data = Es.WebGeter(self.url)
        self.data = {}
        t = self.raw_data.raw_data.find(name="div",id = "tag_browse_global").findAll(name = "div",attrs = {"class":"tag_browse_tag"})
        for i in range(0,len(t)):
            self.data[self.raw_data.raw_data.find(name="div",id = "tag_browse_global").findAll(name = "div",attrs = {"class":"tag_browse_tag"})[i].get("data-tagid")] = self.raw_data.raw_data.find(name="div",id = "tag_browse_global").findAll(name = "div",attrs = {"class":"tag_browse_tag"})[i].string

    def update(self):
        with open ("taglist.json","w") as f:
            json.dump(self.data,f)

def GetInfo(name_str):
    print("name: " + str(name_str))
    temp_info = GetURLbyName(name_str)
    print("URL: " + str(temp_info.run()))
    temp_dict = Es.detailsDataGeter(temp_info.run())
    temp_dict.detailsGeterFixed()
    print("Info: " + str(temp_dict.data))
    return temp_dict.data

def GetURL(name_str):
    temp_info = GetURLbyName(name_str)
    return temp_info.run()

if __name__ == '__main__':
    print(GetInfo('Mortal Kombat X'))
    print(GetURL('Mortal Kombat X'))


