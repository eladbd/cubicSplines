import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff,sin,cos


def f(x):
    return (sin(x) + cos(x))**(1/3)

# def z_calc():
#
# def c_calc():
#
# def d_calc():


if __name__ == '__main__':
    x = symbols('x')
    # a = math.pi/2
    fx = f(x)
    dfx = diff(f(x))
    print(f'fx is :{fx} dfx is {dfx}')
