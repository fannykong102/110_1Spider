# -*- coding: utf-8 -*-
"""
Created on Wed Nov  3 06:02:49 2021

@author: fanny
"""

import os
import urllib.request
import requests
from bs4 import BeautifulSoup


path = "images"
if not os.path.isdir(path):
    os.mkdir(path)
    
headers = {"content-type" : "text/html;charset=UTF-8","user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

url = "https://www.pixivision.net/zh-tw/a/1969"
r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "lxml")

list_image = []

picAll = soup.find_all(attrs={"class" : "fab__image-block__image"})
for i in picAll:
    pic = i.find("img")
    list_image.append(pic["src"])

for i in range(len(list_image)):
    urlImage = list_image[i]
    response = urllib.request.urlopen(urlImage)
    ad = "images\\pic" + str(i) + ".jpg"
    fpImg = open(ad, "wb")
    size = 0

    while True:
        info = response.read(10000)
        if len(info) < 1:
            break
        size = size + len(info)
        fpImg.write(info)
    print(size, "image" + str(i) + "dowload")
    fpImg.close()
    response.close()
