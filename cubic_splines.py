import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, sin, cos


def f(x):
    return (sin(x) + cos(x)) ** (1 / 3)


def z_calc(n):
    for i in (0,n-1):



def c_calc(y, h, z):
    return y / h - z * h / 6


def d_calc(y_p1, h, z_p1):
    return y_p1 / h - z_p1 * h / 6


if __name__ == '__main__':
    x = symbols('x')
    # a = math.pi
    fx = f(x)
    dfx = diff(f(x))
    print(f'fx is :{fx} dfx is {dfx}')
