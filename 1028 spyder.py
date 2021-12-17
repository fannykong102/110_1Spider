import requests
from bs4 import BeautifulSoup

url="https://zh.wikipedia.org/wiki/2019%E5%86%A0%E7%8B%80%E7%97%85%E6%AF%92%E7%97%85%E5%85%A8%E7%90%83%E5%90%84%E5%9C%B0%E7%96%AB%E6%83%85"
r=requests.get(url)
r.encoding="utf8"
soup=BeautifulSoup(r.text,"lxml")
file = open("wikipediadata.csv","w",encoding="utf8")
tag_div=soup.find(id="covid19-container")
tag_table=tag_div.find(name="table")
tag_str=tag_table.text
str0=str(tag_str.replace(",",""))
#str0 = str0.replace(",", "")
str0 = str0.split("\n\n")
str1 = []
for i in str0:
    if i != "":
        str1.append(i)
print(str1)

fileO = open("test.csv", "w", encoding="utf8")
strALL = ""
for i in str1:
    strALL += i + ","
fileO.write(strALL)
fileO.close()
#file.write(str1)
#file.close()
