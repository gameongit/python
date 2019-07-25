#/usr/bin/python

def solution(A):
   n = len(A)
   P = [0] * (n + 1)
   print P
   for k in range(1, n + 1):
       P[k] = P[k - 1] + A[k - 1]
   print P

LIST=[0, 1, 0, 1, 1]
solution(LIST)
                   
           
       
