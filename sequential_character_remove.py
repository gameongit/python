#!/usr/bin/python

DOCSTRING=''' To remove the sequential duplicate characters in the lis.
original = [a, x, b, b, x, d]
output = [a, d]
'''
LIST = ["a", "x", "b", "b", "x", "d"]
print LIST

def inner_repeat_loop():
    for i in range(len(LIST)):
        if i < (len(LIST)-1) and LIST[i] == LIST[i+1]:
             LIST.remove(LIST[i+1])
             LIST.remove(LIST[i])
        elif i == (len(LIST)-1) and LIST[i-1] == LIST[i]:
             LIST.remove(LIST[i-1])
             LIST.remove(LIST[i])

def sequential_char_remove():
    inner_repeat_loop()
    inner_repeat_loop()
    return LIST

print(sequential_char_remove())
