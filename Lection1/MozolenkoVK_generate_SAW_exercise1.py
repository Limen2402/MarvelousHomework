steps = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def generate_SAW(cache):
    c = []
    for a in cache:
        for dr in steps:
            b = a.copy() 
            b.append((a[-1][0] + dr[0], a[-1][1] + dr[1]))
            if b.count(b[-1]) == 1: # по сравнению с предыдущей задачей добавлено только это условие
                c.append(b)
    return c


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

    print((i, n, sum_x / n, sum_y / n, sum_r_square / n)) #дополнительно выводится (сразу после номера шага) число путей

##################################################################3

cache = [[(0, 0)]]
L = 13

for i in range(0, L):
    output(i, cache)
    cache = generate_SAW(cache)
output(L, cache)


# по первым точкам average_square_radius ~ L ^ 1.42. Интернет вообще говорит, что проблема эта сложная, одни предположения. 
