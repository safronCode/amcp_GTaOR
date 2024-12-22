import numpy as np
from simplex_method import *


def branch_and_bound(c, A, b, sign):
    """
    Решение задачи целочисленного линейного программирования методом ветвей и границ.

    Параметры:
    - c: коэффициенты целевой функции (1D массив).
    - A: матрица ограничений (2D массив).
    - b: правая часть ограничений (1D массив).
    - sign: строка знаков ограничений (1D массив).

    Возвращает:
    - Оптимальное значение целевой функции (или None, если нет решения).
    - Оптимальный вектор решений (или None, если нет решения).
    """
    check_point = np.array([0, 0])
    for mode in [1, -1]:
        point, fval = simplex_method(mode * c, A, b, sign)
        check_point = np.vstack([check_point, point])
    check_point = np.delete(check_point, (0), axis=0)

    if not ((np.abs(np.floor(check_point[0]) - np.floor(check_point[1])) >= 1).all()):
        print('Задача не имеет целочисленных решений')
        return None, None

    queue = [(c, A, b, sign)]
    best_solution = None
    best_value = -np.inf

    while queue:
        current_c, current_A, current_b, current_sign = queue.pop(0)
        res = simplex_method(current_c, current_A, current_b, current_sign)
        x = res[0]
        if np.allclose(x, np.round(x)):
            value = res[1]
            if value > best_value:
                best_value = value
                best_solution = x
            break

        else:
            fractional_index = np.argmax(np.abs(x - np.round(x)))
            fractional_value = x[fractional_index]

            new_sign = np.append(current_sign, 1)

            lower_A = np.vstack([current_A, np.zeros(len(current_c))])
            lower_A[-1, fractional_index] = 1  # x[fractional_index] <= floor(fractional_value)
            lower_b = np.append(current_b, np.floor(fractional_value))

            upper_A = np.vstack([current_A, np.zeros(len(current_c))])
            upper_A[-1, fractional_index] = -1  # x[fractional_index] >= ceil(fractional_value)
            upper_b = np.append(current_b, -np.ceil(fractional_value))

            queue.append((current_c, lower_A, lower_b, new_sign))
            queue.append((current_c, upper_A, upper_b, new_sign))

    return best_solution, best_value
