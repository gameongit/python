#!/usr/bin/python

import random, sys

usernum = int(input("Enter your number to guess between 0 to 9: "))
if usernum > 9:
   print("Your number is not in the range")
   exit()

x = random.randint(1,9)
print(x)
if x == usernum:
   print("You guess the right number")
elif x > usernum:
   z = x - usernum
   if z >= 5:
        print("Your number is too low")
   elif z >= 3 and z < 5:
        print("Your number is low")
   elif z >= 1 and z < 3:
        print("Your number is very near")
elif x < usernum:
   z = usernum - x
   if z >= 5:
        print("Your number is too high")
   elif z >= 3 and z < 5:
        print("Your number is high")
   elif z >= 1 and z < 3:
        print("Your number is very near")
