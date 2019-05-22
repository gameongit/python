#!/usr/bin/python3.6

def prime_number_till(num):
    LIST = []
    RANLIST = []
    for i in range(2, int(num)+1):
        for x in range(2, (i/2)+1):
             if i % x == 0:
                break
        else:
             LIST.append(i)

    return LIST     

def prime_number_or_not(num1):
    for ran in range(2, (num1/2) + 1):
         if num1 % ran == 0:
             return (str(num1)+" is not prime")
             break
    else:
         return (str(num1)+" is prime")

NUM = int(raw_input("Enter the number to check : "))
print("Below are the prime numbers till "+str(NUM))
print(prime_number_till(NUM))
print(prime_number_or_not(NUM))


