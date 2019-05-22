#!/usr/bin/python

import random

#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
BIGLIST = []
LIST = []
def original_list():
    for i in range(20):
        BIGLIST.append(random.randint(0, 20))
    return BIGLIST

def less_than_10():
   for x in BIGLIST:
      if x < 10:
         LIST.append(x)
   return LIST

print("Original list is : ")
print(original_list())
print("List which is less than 10 : ")
print (less_than_10())


