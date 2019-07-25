#!/usr/bin/python
import random

'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list. For practice, write this code inside a function.
'''
list1 = []
#newlist = []
for x in range(10):
    c = random.randint(1, 101)
    list1.append(c)

print(list1)
def list_ends(a_list):
    return [a_list[0], a_list[-1]]

print(list_ends(list1))

