# -*- coding: utf-8 -*-
"""Practice#1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zUfxHvny5a34N7peLgEhWbP2pAC4AEJE
"""

# Cryptography 

n = int(input("Shift? "))
pt = input("Input a sentence: ")
ct = ''

for i in pt:
  c = i
  if i.isalpha() == True:
    an = ord(i) + n
    c = chr(an)
  
  ct = ct + c

print(ct)

