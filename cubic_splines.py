import math
import matplotlib.pyplot as plt
import numpy as np
from sympy import symbols, diff, sin, cos, sqrt

xi = np.empty(5)
yi = np.empty(len(xi))

def f(x):

    return np.sign(sin(x) + cos(x)) * np.abs(sin(x) + cos(x)) ** (1/3)
    # return sqrt(x)

def z_calc():
    n = len(xi)
    b = np.empty(n)
    u = np.empty(n)
    v = np.empty(n)
    Z = np.empty(n)
    h = np.empty(n - 1)
    # initialize
    for i in range(0, n - 1):
        h[i] = xi[i + 1] - xi[i]  # plus or minus?????
        b[i] = (6 / h[i]) * (yi[i + 1] - yi[i])
    u[1] = 2*(h[0] + h[1])
    v[1] = b[1] - b[0]
    Z[0] = Z[-1] = 0
    # classification
    for i in range(2, n - 1):
        u[i] = 2 * (h[i] + h[i - 1]) - ((h[i - 1]) ** 2) / u[i - 1]
        v[i] = b[i] - b[i - 1] - ((h[i - 1]) ** 2) / (u[i-1] * v[i - 1])
    # solving top to bottom
    for i in range(n - 2, 0, -1):
        Z[i] = (v[i] - h[i] * Z[i + 1]) / u[i]
    # print(Z)
    return Z, h


def c_d_calc(h, Z):
    n = len(xi)
    C = np.empty(n - 1)
    D = np.empty(n - 1)
    for i in range(len(C)):
        C[i] = yi[i+1]/h[i] - (Z[i+1]*h[i])/6
        D[i] = yi[i] / h[i] - (Z[i] * h[i]) / 6
    return C, D

def aaa():
    Z, h = z_calc()
    C, D = c_d_calc(h, Z)
    return Z, h, C, D

def S(x, Z, h, C, D):
    for i in range(len(xi) - 1):
        if x >= xi[i] and x <= xi[i+1]:
            return (Z[i] / (6 * h[i]))*(xi[i+1] - x)**3 + (Z[i+1]/(6 * h[i]))*(x - xi[i])**3 + C[i]*(x - xi[i]) + D[i]*(xi[i + 1] - x)
    print(x, " is not in range.")

if __name__ == '__main__':

    xi = np.linspace(-6, 6, 5)
    print(xi)
    for i in range(len(xi)):
        yi[i] = f(xi[i])

    Z, h, C, D = aaa()

    axisX = np.linspace(xi[0], xi[-1],(int)(xi[-1] - xi[0])*50)
    cubicY = np.empty(len(axisX))
    funcY = np.empty(len(axisX))
    for i in range(len(axisX)):
        cubicY[i] = S(axisX[i], Z, h, C, D)
        funcY[i] = f(axisX[i])


    plt.plot(axisX, cubicY)
    plt.plot(axisX, funcY)
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.legend(['Cubic Splines', 'Original function'])
    plt.grid()
    plt.title('Cubic Splines')
    plt.show()

