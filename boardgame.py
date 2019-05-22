#!/usr/bin/python3.6

a=" ---"
b="|   "

c=int(raw_input("Enter the size of pattern : "))
for i in range(1,(c+1)):
   print(a*c)
   print(b*(c+1))
   print(a*c)

