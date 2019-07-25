#/usr/bin/python

'''
given a non-empty array A, returns the value of the maximal product of any triplet.

For example, given array A such that:

  A[0] = -3
  A[1] = 1
  A[2] = 2
  A[3] = -2
  A[4] = 5
  A[5] = 6
the function should return 60, as the product of triplet (2, 4, 5) is maximal.
'''


def solution(A):
    MAX=[]
    if len(A) < 3:
       return -1
    else:
       Asort = sorted(A)
       R = Asort[-3] * Asort[-2] * Asort[-1] 
       MAX.append(R)
       R = Asort[0] * Asort[1] * Asort[-1]
       MAX.append(R)
       return max(MAX)

LIST=[-3, 1, 2, -2, 5, 6]
solution(LIST)
