#!/usr/bin/python
from __future__ import division

print ("The compount interest on the amount deposited yearly for a fixed time interval")
print ("Enter the amount:")
Princ = int(input())
print("Enter the rate of interest:")
RateOfInterest = int(input())
print("Enter the number of years:")
Years = int(input())
yr = 1
princ = Princ
HH = ((100 + RateOfInterest) / 100)
PO = pow(HH, Years)
while yr <= Years:
     amount = int(princ * ((100 + RateOfInterest) / 100))
     print ("The CI for ", yr, "year is :", amount)
     yr += 1
     princ = amount + Princ
print('The CI for this amount is :', amount)
print("The CI for the principle ", Princ, " for ", Years, "on ", RateOfInterest, "rate of interest is: ", amount)
