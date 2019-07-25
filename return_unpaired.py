#/usr/bin/python

'''
We have a given array A consisting of N integers fulfilling the above conditions, returns the value of the unpaired element.

For example, given array A such that:

  A[0] = 9  A[1] = 3  A[2] = 9
  A[3] = 3  A[4] = 9  A[5] = 7
  A[6] = 9
the function should return 7
'''

def solution(A):
    print sorted(LIST)
    if len(A) == 1:
       return A[0]
    else:
       A = sorted(A)
       for i in range(1, len(A)+1):
           if i+1 == len(A) and A[i-1] != A[i]:
                print A[i]
           elif i-1 < len(A)-1 and A[i-1] != A[i] and A[i] != A[i+1]:
                print A[i]




'''
def solution(A):
    print LIST
    result = 0
    for number in A:
        result ^= number
    print result
'''

LIST = [ 1, 2, 1, 2, 3, 4, 5, 4, 3, 5, 6, 7, 8, 9, 9, 7, 8] 
#LIST = [2, 2, 3, 3, 4] 
solution(LIST)
    

