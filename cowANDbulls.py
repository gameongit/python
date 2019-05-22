#!/usr/bin/python

import random


def compare_num(number, user_guess):
    cowbull = [0,0] # cow , bull
    for i in range(len(number)):
        if number[i] == user_guess[i]:
             cowbull[1] += 1
        else:
             cowbull[0] += 1
    return cowbull

if __name__=="__main__":
    playing = True
    number = str(random.randint(1000,9999))
    guesses = 0
 
    print("Let's play a game of Cowbull!") #explanation
    print("I will generate a number, and you have to guess the numbers one digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = raw_input("Give me your best guess in 4 digit number like 1234 : ")
        if user_guess == "exit":
           break
        cowbullcount = compare_num(number, user_guess)
        guesses+=1

        print("You have "+ str(cowbullcount[0])+" cows, and " + str(cowbullcount[1]) + " bulls.")
        
        if cowbullcount[1]==4:
            playing = False
            print("You win the game after "+ str(guesses)+ "! The number was "+str(number))
            break
        else:
            print("Your guess isn't quite right, try again.")
