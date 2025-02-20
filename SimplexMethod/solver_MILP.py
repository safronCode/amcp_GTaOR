from package.methods.branch_bound import *
from package.linker import *
from scipy.optimize import linprog

'''
    Решение задачи целочисленного линейного программирования с помощью метода ветвления и границ и симплекс-метода .

    Параметры:
    - c: коэффициенты целевой функции (1D массив).
    - A: матрица ограничений (2D массив).
    - b: правая часть ограничений (1D массив).
    - sign: строка знаков ограничений (1D массив).

    Возвращает:
    - Оптимальное значение целевой функции (или None, если функционал не достигает экстремума).
    - Оптимальный вектор решений (или None, если функционал не достигает экстремума).
'''

rows, columns, rhs, bounds, integer_variables = parse_mps(path2mpc + 'gen-ip036.mps')  # path2mpc см. в package.helpers
c = get_c(columns)
b = get_b(rhs)
A = get_A(columns, len(b), len(c))
bounds = np.array([(0, None)] * len(c))


fval, point = branch_and_bound(c, A, b, bounds)
print('\033[21mРешение с помощью симплекс-метода (amcp):\n\033[0m\t\t\033[31m\033[21mMinimization\033[0m')
print(f'Экстремальное значение функции: {-fval}')
print(f'В точке x* : {point}')

res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
fval = res.fun
point = res.x

print('\033[21mРешение с помощью симплекс-метода:\n\033[0m\t\t\033[31m\033[21mMinimization\033[0m')
print(f'Экстремальное значение функции: {fval}')
print(f'В точке x* : {point}')
