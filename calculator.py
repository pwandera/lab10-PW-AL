# https://github.com/pwandera/lab10-PW-AL.git
# Partner 1: Paul Wandera
# Partner 2: Angel Lopez-Santiago

import math

def square_root(a):
    if a < 0:
        raise ValueError
    else:
        return math.sqrt(a)

def hypotenuse(a, b):
    return math.hypot(a, b)

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