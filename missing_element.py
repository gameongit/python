#/usr/bin/python
'''
given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.
'''
'''
def solution(A):
   A = sorted(A)
   if len(A) == 0:
      A.insert(0, 1)
      return A[0]
   elif len(A) == 1:
      return A[0]+1
   elif len(A) == 2:
      return A[0]+1
   else:
      for i in range(1, A[-1]+1):
         if i not in A:
            return i
#          if i <= len(A)-2 and A[i+1] - A[i] != 1:
#              return A[i]+1


#       if A[i+1] == len(A) and A[i+1]-1 != A[i]:
#           print A[i+1] - A[i]          
#       elif A[i+1] < len(A) and A[i] != A[i+1]-1:
#           print A[i+1] - A[i]
''' 
def solution(A):

    n = len(A)+1
    result = n * (n + 1)//2

    return result - sum(A)

LIST=[2, 3, 4, 5, 7, 8, 9]
print(solution(LIST))
