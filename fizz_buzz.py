#!/usr/bin/python3.6

'''
Enter a number, If the number is divisible by 3 then Buzz will display and if divisible by 5 then display Fizz and if number is divisible by both 3 and 5 then it will show the number. 
'''

def fizz_buzz(x):
    d = bool(x % 5)
    f = bool(x % 3)
    if not d and not f:
       return ("FizzBuzz")
    elif not d and f:
       return ("Fizz")
    elif not f and d:
       return ("Buzz")
    else:
       return x

print(fizz_buzz(int(raw_input("Enter the number : "))))

