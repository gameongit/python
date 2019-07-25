#/usr/bin/python

def solution(A, B):
# Check if number is present in the bigger number
     if str(A) in str(B):
# print the length of series for checking the index for the number and then find the index of the number using if condition.
        result = [n for n in range(len(str(B))) if str(B).find(str(A), n) == n]
        result = [int(i) for i in result]
        return result
 #           return int(i)
#        for i in range(len(result)):
#           return result[i]
     else:
        return -1

num = 53
number = 19537865367
print(solution(num, number))
