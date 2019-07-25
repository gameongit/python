#!/usr/bin/python

import os, sys, math

def test(): 
     print ("Hello World!, How are you ?")
     f= open("/tmp/guru99.txt","w+")
     f.write("Appended line")
     f.close()

test ()

