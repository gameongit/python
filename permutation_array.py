#/usr/bin/python

'''
given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0
'''

def solution(A):
   if len(A) == 0:
      return 0
   else:
      max_ele = max(A)
      if max_ele - len(A) > 1:
         return 0
      actual_sum = sum(A)
      check_sum = sum(range(1, len(set(A)) + 1))
      if actual_sum != check_sum:
         return 0
      else:
         return 1

LIST=[4, 1, 3]
solution(LIST)
