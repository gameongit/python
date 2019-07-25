#!/usr/bin/python
import sys

'''
This program will show you the odd and even numbers in a range. 
'''

def showNumbers(limit):
    for i in range(limit + 1):
        if i % 2 == 0:
           print (str(i) + " EVEN")
        else:
           print (str(i) + " ODD")

showNumbers(int(raw_input("Enter the limit : ")))

