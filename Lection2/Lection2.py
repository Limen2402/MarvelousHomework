# Нелинейные уравнения
# 
import numpy as np
import matplotlib.pyplot as plt
# 
# plt.xkcd()
# 
# def f(x):
#     return x ** 3 - 3 * x ** 2 + 5
# 
# xx = np.linspace(-2, 5)
# fig, ax = plt.subplots()
# ax.axvline(0, ls = '--', lw = 1)
# plt.axhline(0, ls = '--', lw = 1)
# ax.plot(xx, f(xx))
# 
# plt.show()      
# Методы: бисекция, секущие, ложные положения, Риддера, обратная параболическая интерполяция
# Метод Брента
# 
# from scipy.optimize import brentq
# xp = brentq(f, -1.8, -0.3)
# 
# print(xp, f(xp))

def f(x):
    return x ** 3 + 1 
def g(x):
    return 3 * x ** 2
epsilon = 0.01

def find_root(f, g, x_0, epsilon):
    x_1 = x_0
    while True:
        x_2 = x_1 - f(x_1) / g(x_1)
        if abs(x_2 - x_1) < epsilon / 2:
            break
        x_1 = x_2
    return x_2

# for i in range(-5, 5):
#     for k in range(-5, 5):
#         print(find_root(f, g, i + k *(1j), epsilon))

# x = [1, 2, 3, 4]
# y = [4, 5, 6, 7]
# fig, ax = plt.subplots()
# ax.plot(x, y, 'o')

x = [- 1 + 0j, 0.5 + 0.866j, 0.5 - 0.866j]
a_x = [[], [], []]
a_y = [[], [], []]
n = 500

for i in range(-n, n, 1):
    for j in range(-n, n, 1):
        if i == 0 and j == 0:
           continue
        y = find_root(f, g, i / n + j *(1j) / n, epsilon)
        for k in range(len(x)):
            if abs(y - x[k]) < 2 * epsilon:
                a_x[k] += [i]
                a_y[k] += [j]

fig, ax = plt.subplots()
ax.set_aspect('equal')
for i in range(len(x)):
    ax.plot(a_x[i], a_y[i], 'o')
plt.show()
#