import numpy

def f(a, x):
    z = 0
    for i in range(a.size):
        z += a[::-1][i] * (x ** i)
    return z + x ** a.size

def g(a, x):
    z = 0
    for i in range(1, a.size):
        z += i * a[::-1][i] * (x ** (i - 1))
    return z + a.size * (x ** (a.size - 1))

def newton_root(f, g, a, x_0, epsilon):
#    x_1 = x_0
#    while True:
#        x_2 = x_1 - f(a, x_1) / g(a, x_1)
#        if abs(x_2 - x_1) < epsilon / 2:
#            break
#        x_1 = x_2
#    return x_2
    return x_0 - f(a, x_0) / g(a, x_0)
#
a = numpy.array([-15, 85, -225, 274, -120])
A = numpy.zeros((a.size, a.size))
epsilon = 10**-5

A[:, -1] = -a[::-1]
for i in range(1, a.size):
    A[i, i - 1] = 1
#print(A)
roots = numpy.linalg.eigvals(A)
new_roots = []
print(roots)

for i in roots:
    new_roots.append(newton_root(f, g, a, i, epsilon))

print(new_roots)