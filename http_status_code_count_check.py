#!/usr/bin/python

'''
This script wil provide you the status of all http state from the file and the number of the states
'''

def count_status_code(file):
    COUNT = {}
    FILE = open(file, "r")
    for line in FILE:
	if "HTTP/1.1" in line:
            COLUMN = line.split(" ")
	    if str(COLUMN[1]) in COUNT:
  	        COUNT[COLUMN[1]] +=1
	    else:
	        COUNT[COLUMN[1]] = 1
    return COUNT
			
print(count_status_code("/tmp/logfile"))
