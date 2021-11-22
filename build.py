#!/usr/bin/python3

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if(b != 0):
        return a / b
    return 0

def mean(l):
    if(len(l) != 0):
        return sum(l) / len(l)
    return 0
