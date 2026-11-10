# https://github.com/henrye122/lab11-HE-ZZ-1-.git
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.
"""
# First example
# Partner 1: Henry Edinger
# Partner 2: Zhouqiao Zhao

import math

def square_root(a):
    try:
        return math.sqrt(a)
    except ValueError:
        raise ValueError(
            "Cannot take the square root of a negative number."
        ) from None

def hypotenuse(a, b):
    try:
        return math.hypot(a, b)
    except TypeError:
        raise ValueError("Both sides must be numbers.") from None

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return b / a


def logarithm(a, b):
    if a <= 0 or a == 1:
        raise ValueError("The base must be positive and cannot equal 1.")
    if b <= 0:
        raise ValueError("The argument must be positive.")
    return math.log(b, a)


def exp(a, b):
    return a ** b