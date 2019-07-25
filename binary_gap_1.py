#/usr/bin/python

'''
For a given positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5. Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps
'''

#Simplest Solution:
def solution(N):
    print bin(N)[2:]
    print len(max(bin(N)[2:].strip('0').strip('1').split('1')))

solution(int(raw_input("Enter the number to convert the binary: ")))
