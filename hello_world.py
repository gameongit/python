#!/usr/bin/python
import sys

def hello_world():
   n = 0
   while True:
      print ("This is a test check " + str(n))
      n += 1
      if n > 9:
         break


hello_world()
