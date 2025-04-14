import math

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a*b

def divide(a,b):
    if a == 0:
        raise ValueError
    else:
        return b/a

def logarithm(a,b):
    if b <= 0:
        raise ValueError
    else:
        return math.log(b,a)

def exponent(a,b):
    return a ** b





