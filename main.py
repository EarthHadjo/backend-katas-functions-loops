#!/usr/bin/env python
"""Implements math functions without using operators except for '+' and '-' """

__author__ = "earthhadjo"

import sys


def add(x, y):
    """Add two integers. Handles negative values."""
    return(x + y)


def multiply(x, y):
    """Multiply x with y. Handles negative values of x or y."""
    if y < 0:
        result = -multiply(x, -y)
    elif y == 0:
        result = 0
    elif y == 1:
        result = x
    else:
        result = x + multiply(x, y - 1)
    return(result)


def power(x, n):
    """Raise x to power n, where n >= 0"""
    total = x
    i = 1
    while i < n:
        x = multiply(total, x)
        i += 1
    return(x)


def factorial(x):
    """Compute factorial of x, where x > 0"""
    n = 1
    i = 1
    while i <= x:
        n = multiply(n, i)
        i += 1
    return(n)


def fibonacci(n):
    """Compute the nth term of fibonacci sequence"""
    x = 0
    y = 1
    i = 0
    for i in range(n):
        x = y
        y = i
        i = add(x, y)
    return(i)


def main():
    print(add(2, 4))
    print(multiply(6, -8))

    print(power(2, 8))
    print(factorial(4))
    print(fibonacci(8))


if __name__ == '__main__':
    main()
