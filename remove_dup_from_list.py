#!/usr/bin/python

import random

'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
'''

list1 = []
list2 = []
for x in range(10):
    z = random.randint(1, 10)
    list1.append(z)

for i in list1:
    if i not in list2:
       list2.append(i)

print(list1)
print(list2)
