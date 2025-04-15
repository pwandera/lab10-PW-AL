import math

def add(a, b): 
    return a + b

def subtract(a,b):
    return a - b

def logarithm(a,b):

    if b <= 0 or a <= 0 or a == 1:

        raise ValueError
    else:
        return math.log(b,a)

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError
    return b/a

def exp(a, b):
    return a ** b