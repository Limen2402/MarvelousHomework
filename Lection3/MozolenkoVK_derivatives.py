import cmath, matplotlib.pyplot as plt, numpy

#1. машинная точность

eps = 1.0
while 1 + eps != 1:
    eps /= 10.0
print(eps)

#2. функцию не придумал

#3, 4. станем вычислять производную синуса в точке pi/3. Вот так вот. Программа выдает график, в котором приведены расчеты с пары 
#+ довольно необычный результат для мнимого способа + ридчардсон, у которого хорошо виден показатель 4. Очевидно же. 
  
def f(x):
    return cmath.sin(x)

def f_prime(x):
    return cmath.cos(x)

def f_right(x_0, h):
    return (f(x_0 + h) - f(x_0)) / h

def f_center(x_0, h):
    return (f(x_0 + h) - f(x_0 - h)) / (2 * h)

def f_imag(x_0, h):
    return f(x_0 + h * (1j)).imag / h

def f_rich(x_0, h, q):
    return (q ** 2 * f_center(x_0, h / q) - f_center(x_0, h)) / (q ** 2 - 1)

q = 2
x_0 = cmath.pi / 3
y_true = f_prime(x_0)
N = 100
hh = numpy.logspace(0, -15, N).tolist()

plt.subplot(2, 1, 1)
plt.title('pressision for f = sin in x = pi/3')
plt.xlabel('step')
plt.ylabel('pressision')
plt.grid()
plt.loglog(hh, [abs(y_true - f_right(x_0, h)) for h in hh], 'o--', label = 'right', color = 'b')
plt.loglog([eps ** (1/2), eps ** (1/2)], [1, 10 ** -16], color = 'b')
plt.loglog(hh, [abs(y_true - f_center(x_0, h)) for h in hh], 'o--', label = 'center', color = 'r')
plt.loglog([eps ** (1/3), eps ** (1/3)], [1, 10 ** -16], color = 'r')

plt.loglog(hh, [abs(y_true - f_imag(x_0, h)) for h in hh], 'o--', label = 'imag', color = 'g')

plt.loglog(hh, [abs(y_true - f_rich(x_0, h, q)) for h in hh], 'o--', label = 'richardson', color = 'y')
plt.loglog([eps ** (1/6), eps ** (1/6)], [1, 10 ** -16], color = 'y')

plt.legend()

#5. у нас тут проблема, в нуле вторая происзводная x^2 ln x беспардонно расходится. вам три последовательных метода, 
#которые должны улучшать точность, но они не работают

def f(x):
    if (x > eps):
        return x ** 2 * cmath.log(x)
    else:
        return 0

def f_prime(x):
    if (x > eps):
        return x + 2 * x * cmath.log(x)
    else:
        return 0


def f_right(x_0, h):
    return (f(x_0 + h) - f(x_0)) / h

def f_right_2(x_0, h):
    return (-1.5 * f(x_0) + 2 * f(x_0 + h) - 0.5 * f(x_0 + 2 * h)) / h

def f_right_3(x_0, h):
    return (-(11/6) * f(x_0) + 3 * f(x_0 + h) - 1.5 * f(x_0 + 2 * h) + (1/3) * f(x_0 + 3 * h)) / h



x_0 = 0.0001
y_true = f_prime(x_0)

plt.subplot(2, 1, 2)
plt.loglog(hh, [abs(y_true - f_right(x_0, h)) for h in hh], 'o--', label = 'simple O(h)', color = 'r')
plt.loglog(hh, [abs(y_true - f_right_2(x_0, h)) for h in hh], 'o--', label = 'advanced O(h^2)', color = 'b')
plt.loglog(hh, [abs(y_true - f_right_3(x_0, h)) for h in hh], 'o--', label = 'advanced+ O(h^3)', color = 'y')


plt.title('f\' pressision for f = x^2 ln(x) in x_0 = 0.0001')
plt.xlabel('step')
plt.ylabel('pressision')
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()
