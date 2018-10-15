import heapq, matplotlib.pyplot as plt

# Что такое число шагов? Чтобы это было чем-то осмысленным и для классического метода, и для
# "динамического". Поэтому возьмем за него число квадратов апроксимации с шагом *2. Первым делом нарисуем график
# ошибки для стандартного способа

N_start = 2
N_log_range = 10
a = 0.0
b = 1.0

def f(x):
    """any function"""
    return 4 * x ** 3

def cheat_int(a, b):
    """for f(x) = 4x^3"""
    return b ** 4 - a ** 4

def classical_int(f, a, b, N):
    """ simple sum """
    S = 0
    h = (b - a) / N
    for i in range(N):
        x = a + (i + 1/2) * h
        S += h * f(x)
    return S

hh = [N_start * 2 ** i for i in range(N_log_range)]

plt.title('integrate pressision')
plt.xlabel('number of steps')
plt.ylabel('pressision')
plt.grid()
plt.loglog(hh, [abs(cheat_int(a, b) - classical_int(f, a, b, h)) for h in hh], 'o--', label = 'classic', color = 'b')

#создаем затравочные списки
zz = []
h = (b - a) / N_start
heap = [(-abs(f(a + (i + 1/2) * h) * h), a + i * h, a + (i + 1) * h) for i in range(N_start)]
#хипуем
heapq.heapify(heap)

#теперь: прогоняем алгоритм все разы, и если номер шага внезапно нужный - выписываем ответ в zz
for i in range(N_start, N_start * 2 ** N_log_range):  
    p = heapq.heappop(heap)
    a1 = p[1]
    b1 = p[2]
    p1 = (-f((3 * a1 + b1) / 4) * (b1 - a1) / 2, a1, (a1 + b1) / 2)
    p2 = (-f((a1 + 3 * b1) / 4) * (b1 - a1) / 2, (a1 + b1) / 2, b1)
    heapq.heappush(heap, p1)
    heapq.heappush(heap, p2)

    if i in hh:
        S = 0
        for k in heap:
            S += -k[0]
        zz.append(abs(S - cheat_int(a, b)))


plt.loglog(hh, zz, 'o--', label = 'adapt', color = 'r')

plt.legend()
plt.show()

#работает оно как-то странно. Очень слабо. 