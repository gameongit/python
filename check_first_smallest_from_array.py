#/usr/bin/python
import random

'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
'''

def solution(A):
    for x in range(1, len(A) + 1):
        for i in A:
           if x > i and x not in A:
                return x
                break
    else:
        return (max(A)+1)

list1 = []

# For Random list of numbers
#for x in range(1, 10000):
#    c = random.randint(1, 10000)
#    list1.append(c)

# For Sequential list of numbers
list1 = [y for y in range(-10, 10)]
#print list1

ARRAY = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 3, 4, 5, 6, 7, 8, 9]
print(solution(ARRAY))
'''

def solution(A):
    SET = set(A)
    ans = 1
    while ans in SET:
       ans += 1
    return ans
