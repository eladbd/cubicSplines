import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, sin, cos, sqrt

hi = []
bi = []
xi = [1, 4, 9]
yi = []
Ui = []
Vi = []
Zi = []


def f(x):
    # return (sin(x) + cos(x)) ** (1 / 3)
    return sqrt(x)


def z_calc(n):
    Zi = [0] * n
    # initialize
    for i in range(0, n - 1):
        hi.append(xi[i + 1] - xi[i])  # plus or minus?????
        bi.append((6 / hi[i]) * (yi[i + 1] - yi[i]))
    Ui.append(2 * (hi[0] + hi[1]))
    Vi.append(bi[1] - bi[0])
    # print(xi)
    print(hi)
    # classification
    for i in range(1, n - 1):
        Ui.append(2 * (hi[i] + hi[i - 1]) - ((hi[i - 1]) ** 2) / Ui[i - 1])
        Vi.append(bi[i] - bi[i - 1] - ((hi[i - 1]) ** 2) / Ui[i] * Vi[i - 1])
    # solving top to bottom
    for i in range(n - 2, 0, -1):
        Zi.insert(i, (Vi[i] - hi[i] * Zi[i + 1]) / Ui[i])
    print(Zi)


def c_calc(y, h, z):
    return y / h - z * h / 6


def d_calc(y_p1, h, z_p1):
    return y_p1 / h - z_p1 * h / 6


if __name__ == '__main__':
    x = symbols('x')
    # a = math.pi
    fx = f(x)
    for i in range(len(xi)):
        # xi.append(i)
        yi.append(fx.evalf(subs={x: i}))
        # print(xi)
    z_calc(len(xi))
    # print(f'fx is :{xi} dfx is {yi}')
