#!/usr/bin/python

INPUT = raw_input("Enter your thoughts : ")
f = open("/tmp/myfile.txt", "w+")
f.write(INPUT)
f.close()

