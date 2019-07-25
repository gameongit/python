#!/usr/bin/python

'''
This is to find the maximum number in two number.
'''

def max_num(x,y):
    if x > y:
       return ("Max number is : "+str(x))
    else:
       return ("Max number is : "+str(y))

F = int(raw_input("Enter first number : "))
S = int(raw_input("Enter second number : "))
print(max_num(F,S))
