#/usr/bin/python

def solution(A):
    if len(A) == 2:
       if A[0] == 0 and A[1] == 1:
          print 1
    else:
       LI = []
       for i in range(0, len(A)):
           if A[i] == 0:
               for j in range(i, len(A)):
                   if A[j] == 1:
                      LI.append((i,j))
    if len(LI) > 1000000000:
       return -1
    else:
       print len(LI)
    
#    ps = prefix_sums(A)
#    print ps

LIST=[0, 1, 0, 1, 1]
solution(LIST)
                   
           
       
