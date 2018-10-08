import cmath, matplotlib.pyplot as plt, numpy

#машинная точность

eps = 1.0
while 1 + eps != 1:
    eps /= 10.0
print(eps)

#функцию не придумал

#станем вычислять производную синуса в точке pi/3. Вот так вот. Программа выдает график, в котором приведены расчеты с пары + довольно необычный расчет для
#мнимого способа
  
def f(x):
    return cmath.sin(x)

def f_prime(x):
    return cmath.cos(x)

def df_right(h, x_0, f, y_true):
    z = (f(x_0 + h) - f(x_0)) / h
    return abs(z - y_true)

def df_center(h, x_0, f, y_true):
    z = (f(x_0 + h) - f(x_0 - h)) / (2 * h)
    return abs(z - y_true)

def df_imag(h, x_0, f, y_true):
    z = f(x_0 + h * (1j)).imag / h
    return abs(z - y_true)

x_0 = cmath.pi / 3
y_true = f_prime(x_0)
N = 100
hh = numpy.logspace(0, -16, N).tolist()

plt.xlabel('step')
plt.ylabel('pressision')
plt.grid()
plt.loglog(hh, [df_right(h, x_0, f, y_true) for h in hh], 'o--', label = 'right', color = 'b')
plt.loglog([eps ** (1/2), eps ** (1/2)], [1, 10 ** -16], color = 'b')
plt.loglog(hh, [df_center(h, x_0, f, y_true) for h in hh], 'o--', label = 'center', color = 'r')
plt.loglog([eps ** (1/3), eps ** (1/3)], [1, 10 ** -16], color = 'r')

plt.loglog(hh, [df_imag(h, x_0, f, y_true) for h in hh], 'o--', label = 'imag', color = 'g')

plt.legend()
plt.show()