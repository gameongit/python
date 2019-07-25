#!/usr/bin/python
import random
DOCSTRING = ''' Check if the pair of the two list makes a sum of 24 or near to it. '''

LIST1 = []
LIST2 = []
def make_list(LIST):
     for i in range(6):
          LIST.append(random.randint(1, 20))

make_list(LIST1)
make_list(LIST2)
print(LIST1)
print(LIST2)

def sum_num(NUM):
    for i in LIST1:
         X = int(NUM) - i
         if X in LIST2:
             print("Pair is ",int(i),int(X)) 

def sum_num1(NUM):
    for i in LIST1:
         X = int(NUM) - i
         if X in LIST2:
             print("Nearest pair is ",int(i),int(X))

sum_num(24)
sum_num1(23)
sum_num1(25)

