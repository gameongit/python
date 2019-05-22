#!/usr/bin/python3.6

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

