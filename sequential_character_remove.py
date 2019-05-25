#!/usr/bin/python
import sys
import random, string
DOCSTRING=''' To remove the sequential duplicate characters in the lis.
original = [a, x, b, b, x, d]
output = [a, d]
'''
LIST = []
for i in range(20):
    LIST.append(random.choice(string.ascii_lowercase))

LIST = ['y', 'w', 'w', 'u', 'j', 'p', 'm', 'f', 'm', 'a', 'd', 'b', 'k', 'p', 'a', 'u', 't', 'y', 'n', 'j']
print LIST

def inner_repeat_loop():
   i = 0
   while i < len(LIST)-1:
      if LIST[i] == LIST[i+1]:
          LIST.remove(LIST[i+1])
          LIST.remove(LIST[i])
          i -= 1
      i += 1

def sequential_char_remove():
    if len(LIST) == 0 or len(LIST) == 1:
        print("The list is not complete to sort")
        exit()
    RANLIST = list(LIST)
    inner_repeat_loop()
    while RANLIST != LIST:
        RANLIST = list(LIST)
        inner_repeat_loop()
    return LIST

print(sequential_char_remove())
