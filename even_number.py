#!/usr/bin/python
DOCSTRING = ''' This is to find the even number
'''
LIST = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
EVEN = []
def even_num(X):
    for i in X:
        if i % 2 == 0:
            EVEN.append(i)
    print EVEN

even_num(LIST)
