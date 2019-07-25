#!/usr/bin/python
import set

def deleteReoccurringCharacters(string):
    seenCharacters = set()
    outputString = ''
    for char in string:
        if char not in seenCharacters:
            seenCharacters.add(char)
            outputString += char
    return outputString

deleteReoccurringCharacters(aabbcc)
