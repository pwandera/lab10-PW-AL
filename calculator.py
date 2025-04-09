import math

def add(a, b): 
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a*b

def divide(a, b):
    try:
        return b/a

    except ZeroDivisionError:
        print('Cannot divide by Zero')

def logarithm(a,b):
    try:
        x = math.log(a, b)
        return x
    except ValueError:
        print('Incorrect inputs')
    except TypeError:
        print('Inputs must be numbers')

def exponent(a,b):
    return a ** b








