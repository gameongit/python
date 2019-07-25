#!/usr/bin/python
from __future__ import division

print ("Enter the amount:")
Princ = int(input())
print("Enter the rate of interest:")
RateOfInterest = int(input())
print("Enter the number of years:")
Years = int(input())
amount = int(Princ * pow(((100 + RateOfInterest) / 100), Years))
print('The CI for this amount is :', amount)
#print("The CI for the principle ", Princ, " for ", Years, "on ", RateOfInterest, "rate of interes is: ", amount)

