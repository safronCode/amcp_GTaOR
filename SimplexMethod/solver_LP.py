from package.linker import *
from scipy.optimize import linprog
import time


'''
    Решение задачи линейного программирования с помощью симплекс-метода.

    Параметры:
    - c: коэффициенты целевой функции (1D массив).
    - A: матрица ограничений (2D массив).
    - b: правая часть ограничений (1D массив).
    - sign: строка знаков ограничений (1D массив).

    Возвращает:
    - Оптимальное значение целевой функции (или None, если функционал не достигает экстремума).
    - Оптимальный вектор решений (или None, если функционал не достигает экстремума).
'''

rows, columns, rhs, bounds, integer_variables = parse_mps(path2mpc + 'gen-ip002.mps') #path2mpc см. в package.helpers
sign = get_sign(rows)
c = get_c(columns)
b = get_b(rhs)
A = get_A(columns, len(b), len(c))


start_time = time.time()
res = linprog(c, A_ub=A, b_ub=b, method='highs')
end_time = time.time()

print("Решение через решатель highs:")
print("Оптимальные значения переменных x:", res.x)
print("Значение целевой функции:", res.fun)
time_scipy = end_time - start_time
print(f"Время выполнения: {time_scipy:.6f} секунд")
print('\n'+'-'*100+'\n')


start_time = time.time()
point, fval = simplex_method(-c, A, b, sign)
end_time = time.time()
formatted_point = [f"{val:.2f}" for val in point]
color_print(f'При заданных условиях --> maximization:', 'RED')
print(f' В точке x*: {formatted_point}\n F(x*) = {-fval:.2f}')
time_amcp = end_time - start_time
print(f"Время выполнения: {time_amcp:.6f} секунд")
