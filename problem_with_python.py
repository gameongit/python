#!/usr/bin/python

def foo(date=[]):
    date.append("today")
    return date

foo()
print(foo())

def foo1(bar=None):
    if bar is None:
       bar = []
    bar.append("today1")
    return bar

foo1()
print(foo1())
