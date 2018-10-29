#cProfile
import math, numpy as np, matplotlib.pyplot as plt, scipy.special as sp,scipy.integrate as int

def f(x, y):
    return math.sin(10 * x) * math.sin(y)

#thanks, symmetries
answer_full = 0
answer_part = 0

#1.double the legendre
n = 5
position_x, weight_x = np.polynomial.legendre.leggauss(n)

position_y = position_x
weight_y = weight_x

sum = 0
for i in range(len(position_x)):
    for j in range(len(position_y)):
        sum += weight_x[i] * weight_y[j] * f(position_x[i], position_y[j])
print(sum)

#2.half jacobi- half legendre - such as i get it

position_y, weight_y = sp.roots_jacobi(n, 0, 0)

sum = 0
for i in range(len(position_x)):
    for j in range(len(position_y)):
        sum += weight_x[i] * weight_y[j] * f(position_x[i], position_y[j]) * position_x[i]
print(sum)

#3.