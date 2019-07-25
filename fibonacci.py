#!/usr/bin/python
import sys

fib = []
n = int(input("Enter the number : "))
def fibo(num):
    if num != 0:
       s = int(input("Number in the series should be : "))
       fib.append(num)
       fib.append(num)
       for x in range(1, s - 1):
          z = fib[x] + fib[x - 1]
          fib.append(z)
    else:
       print("Please start your series with some real number")
       exit() 

fibo(n)
print(fib)
