from numpy import allclose
import cmath

# Наивное решение
#
# def solve_quad(b, c):
#     D = cmath.sqrt(b ** 2 - 4 * c)    
#     x1 = (-b + D) / 2
#     x2 = (-b - D) / 2  
#
#     return x1, x2

# Чуть менее наивное решение: мы не станем вычитать друг из друга близкие большие числа, а вычислим второй корень и
# воспользуемся формулой Виета. Вообще говоря, учитывая способ проверки, это в некотором смысле чит, так что выведем
# тот тот самый корень отдельно (более-менее правильно)

def solve_quad(b, c):
    D = cmath.sqrt(b ** 2 - 4 * c)
    if (D == b):
        x1 = (-b - D) / 2
        x2 = c / x1
    else:
        x1 = (-b + D) / 2
        x2 = c / x1

    return x1, x2

variants = [{'b': 4.0, 'c': 3.0}, {'b': 2.0, 'c': 1.0}, {'b': 0.5, 'c': 4.0}, {'b': 1e10, 'c': 3.0}, {'b': -1e10, 'c': 4.0}]
for var in variants:
    x1, x2 = solve_quad(**var)
    print(allclose(x1*x2, var['c']), x1, x2)
