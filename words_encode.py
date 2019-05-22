#!/usr/bin/python
import string
DATA = raw_input("Enter your word that needs to be encode: ")
LIST = []
ENCODE = []
for num in range(0, 26):
      LIST.append(string.ascii_lowercase[num]) 
      LIST.append(int(num) + 1)

def first_encode(STRING):
     for i in STRING:
         if i in LIST:
             I = LIST.index(i)
             ENCODE.append(LIST[I + 1])
     return ENCODE

print(first_encode(DATA))

