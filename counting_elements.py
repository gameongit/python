#/usr/bin/python

def counting(A, m):
   n = len(A)
   count = [0] * (m + 1)
   for k in range(n):
      count[A[k]] += 1
   return count

LIST = [1, 3, 5, 7]
print(counting(LIST, 2))
