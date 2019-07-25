#/usr/bin/python

'''
given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.
'''


def solution(A):
    if len(A) < 3:
       return 0
    else:
       A=sorted(A)
       for i in range(len(A)-2):
          if A[i] + A[i+1] > A[i+2] and A[i] + A[i+2] > A[i+1] and A[i+1] + A[i+2] > A[i]:
              print 1
              print (A[i],A[i+1],A[i+2])
       else:
          print 0

LIST=[10, 50, 5, 1]
#LIST=[10, 2, 5, 1, 8, 20]
solution(LIST)
