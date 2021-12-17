# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 05:25:42 2021

@author: fanny
"""
import csv

file = open("covid19.csv", "r", encoding="utf8")

csvreader = csv.reader(file)

ls = []

for i in csvreader:
    ls.append(i)

conList = []
deadList = []
for  i in range(2,(len(ls)-2)):
    conList.append(int(ls[i][1].replace(",", "")))
    deadList.append(int(ls[i][2].replace(",", "")))
    
print(conList)
print(deadList)

sumcon = 0
sumdead = 0
for i in range(len(conList)):
    sumcon += conList[i]
    sumdead += deadList[i]
print(str(format(sumcon,",d")),sumdead)