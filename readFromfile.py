#!/usr/bin/python

FILE = raw_input("Enter the name of the file : ")
f = open(FILE, "r")
#print(f.read())
print(f.readline())
f.close()
