#/usr/bin/python

'''
For given three integers X, Y and D, returns the minimal number of jumps from position X to a position equal to or greater than Y.

For example, given:

  X = 10
  Y = 85
  D = 30
the function should return 3, because the frog will be positioned as follows:

after the first jump, at position 10 + 30 = 40
after the second jump, at position 10 + 30 + 30 = 70
after the third jump, at position 10 + 30 + 30 + 30 = 100
'''

def solution(X, Y, D):
    if X == Y:
       D = 0
       print D
    elif Y > X:
       T = (Y - X) % D
       if T == 0:
          print (Y-X)/D
       else:
          print (Y-X)/D + 1

solution(10, 85, 30)
    
