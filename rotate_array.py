#/usr/bin/python

'''
For a given array A consisting of N integers and an integer K, returns the array A rotated K times.

For example, given

    A = [3, 8, 9, 7, 6]
    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]
'''

def solution(A, K):
    if len(A) >= 1:
       for i in range(K):
           A.insert(0, A[-1])
           A.pop()
       print A
    else:
       print A

#LIST = [3, 8, 9, 7, 6]
#LIST = [0, 0, 0]
LIST = []
TIMES = 3
solution(LIST, TIMES)

