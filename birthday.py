#!/usr/bin/python3.6

import json

birthday = {}
f= open('birthdays.json', 'r')
birthday = json.load(f)
for x, y in birthday.items():
   print(x, y)

#def add_entry():
    
#'''
mydict = {
   "Lalit": "16Nov1986",
   "Ram": "23Feb1988",
   "Sunil": "29Jun1990"
}

print("Welcome to the birthday dictionary. We know the birthday of:")
for x in mydict:
   print(x)

t = raw_input("who's brithday do you want to look up?: ")

if t in mydict:
   print("%s's birthday is %s" %(t, mydict[t])) 
else:
   print("Sorry, we don't have bithday information of "+t) 
 
#'''
