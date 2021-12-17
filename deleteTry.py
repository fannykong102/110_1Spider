# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 06:11:24 2021

@author: fanny
"""


# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 04:14:07 2021

@author: fanny
"""


import requests
from bs4 import BeautifulSoup

headers = {"content-type" : "text/html;charset=UTF-8","user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36"}

url = "https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85"
r = requests.get(url, headers = headers)
soup = BeautifulSoup(r.text, "lxml")

t1 = soup.find(attrs={"class" : "wikitable sortable"})
word = ""
listA = []
listh = []

head = t1.find_all("th")
for i in head:
    listh.append(i.text.replace("\n", ""))
listA.append(listh)

body = t1.find("tbody")
bodytr = body.find_all("tr")
for i in bodytr:
    td = i.find_all("td")
    listb = []
    for i in td:
        listb.append(i.text.replace("\n", ""))
    if len(listb) != 0:
        listA.append(listb)
print(listA)
    
for i in listA:
    for j in i :
        word += "\"" + j + "\"" + ","
    word += "\n"

fp = open("covid19_2.csv", "w", encoding="utf8")
fp.write(word)
fp.close()

numlist = []

for i in range(1,len(listA)):
    w = listA[i][1]
    word = ""
    for j in range(len(w)):
        ch = w[j]
        if ch == "[":
            break
        word += ch
    numlist.append(word)
print(numlist)
