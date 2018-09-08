steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# Я искренне считаю рекурсию злом, поэтому выпрямил алгоритм. Теперь нижеследующая функция поедает cache и выдает его же через один шаг.

def generate_walk(cache):
    c = []
    for a in cache:
        for dr in steps:
            b = a.copy() # ненавистные указатели!
            b.append((a[-1][0] + dr[0], a[-1][1] + dr[1]))
            c.append(b)
    return c

#выводящая все на свете функция - выводится номер шага, средний x, средний y и средний квадрат r

def output(i, cache):
    n = len(cache)
    sum_x = 0
    sum_y = 0
    sum_r_square = 0

    for a in cache:
        x, y = a[-1]
        sum_x += x
        sum_y += y
        sum_r_square += x ** 2 + y ** 2

    print((i, sum_x / n, sum_y / n, sum_r_square / n))

##################################################################3

cache = [[(0, 0)]]
L = 10

for i in range(L):
    cache = generate_walk(cache)
    output(i + 1, cache)

#Ответ говорит нам - зависимость замечательная, average_square_radius = L 