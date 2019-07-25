#!/usr/bin/python
DOCSTRING = '''
Find the Divisor of the number
'''
NUM = input("Enter the number: ")
DIVISORLIST = []
X = range(2, NUM)
def divisor():
    for i in X:
        if NUM % i == 0:
            DIVISORLIST.append(i)

    print "List show the divisor of the numbr: "+ str(DIVISORLIST)

divisor()
