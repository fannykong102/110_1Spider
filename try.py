# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 06:35:55 2021

@author: fanny
"""

word = ""
s = "ehhfi[whi"
for i in range(len(s)):
    ch = s[i]
    if ch == "[":
        break
    word += ch
    print(ch)
print(word)