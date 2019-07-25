#!/usr/bin/python
import random

def num():
   LIST = []
   for i in range(10):
      x = random.randint(1, 20)
      if x not in LIST:
         LIST.append(x)
   
   if __name__=="__main__":
      rand_num = random.randint(1, 20)
      if rand_num in LIST:
         return True
      else:
         return False

print(num())
