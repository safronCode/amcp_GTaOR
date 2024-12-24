from package.methods.branch_bound import *
from package.linker import *

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

c = np.array([2, -2])

A = np.array([[1, 0],
              [0, 6/4],
              [6/3.5, 0],
              [1,1]])

b = np.array([4.5, 6, 6, 1])

sign = np.array ([1, 1, 1, -1])

point, fval = branch_and_bound(c, A, b, sign)
print('\033[21mРешение с помощью симплекс-метода (amcp):\033[0m\t\t\033[31m\033[21mMaximization\033[0m')
print(f'Экстремальное значение функции: {fval}')
print(f'В точке x* : {point}')