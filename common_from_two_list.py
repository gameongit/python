#!/usr/bin/python

import random

list1 = []
list2 = []
listcommon = []

for x in range(10):
   y = random.randint(1, 21)
   list1.append(y)
   z = random.randint(1, 21)
   list2.append(z)

print(list1)
print(list2)

for i in list1:
   if i in list2 and i not in listcommon:
      listcommon.append(i)

print(listcommon)
