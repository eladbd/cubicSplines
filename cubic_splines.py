import matplotlib.pyplot as plt
import numpy as np
from sympy import sin, cos

xi = np.empty
yi = np.empty

def f(x):
    return np.sign(sin(x) + cos(x)) * np.abs(sin(x) + cos(x)) ** (1/3)

def z_calc():
    n = len(xi)
    b = np.empty(n)
    u = np.empty(n)
    v = np.empty(n)
    Z = np.empty(n)
    h = np.empty(n - 1)
    # initialize
    for i in range(0, n - 1):
        h[i] = xi[i + 1] - xi[i]
        b[i] = (6 / h[i]) * (yi[i + 1] - yi[i])
    u[1] = 2*(h[0] + h[1])
    v[1] = b[1] - b[0]
    Z[0] = Z[-1] = 0
    # classification
    for i in range(2, n - 1):
        u[i] = 2 * (h[i] + h[i - 1]) - ((h[i - 1]) ** 2) / u[i - 1]
        v[i] = b[i] - b[i - 1] - h[i - 1] / (u[i-1] * v[i - 1])
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

def all_var():
    Z, h = z_calc()
    C, D = c_d_calc(h, Z)
    return Z, h, C, D

def S(x, Z, h, C, D):
    for i in range(len(xi) - 1):
        if x >= xi[i] and x <= xi[i+1]:
            return (Z[i] / (6 * h[i]))*(xi[i+1] - x)**3 + (Z[i+1]/(6 * h[i]))*(x - xi[i])**3 + C[i]*(x - xi[i]) + D[i]*(xi[i + 1] - x)
    print(f"{x} is not in range.")

if __name__ == '__main__':
    for j in [2, 4, 6, 12]:
        xi = np.linspace(-6, 6, j + 1)
        yi = np.empty(len(xi))
        for i in range(len(xi)):
            yi[i] = f(xi[i])

        Z, h, C, D = all_var()

        axisX = np.linspace(xi[0], xi[-1], (int)(xi[-1] - xi[0])*50)
        cubicY = np.empty(len(axisX))
        funcY = np.empty(len(axisX))
        for i in range(len(axisX)):
            cubicY[i] = S(axisX[i], Z, h, C, D)
            funcY[i] = f(axisX[i])


        plt.scatter(xi, yi, color = 'black', zorder = 3, linewidth = 0.1)
        for i_x, i_y in zip(xi, yi):
            plt.text(i_x, i_y, '({:.2f}, {:.2f})'.format(i_x, i_y))
        plt.plot(axisX, cubicY)
        plt.plot(axisX, funcY)
        plt.legend(['Cubic Splines', 'Original function'])
        plt.axhline(linewidth = 1, color = 'black')
        plt.axvline(linewidth = 1, color = 'black')
        plt.grid()
        plt.title('Cubic Splines')
        plt.show()
