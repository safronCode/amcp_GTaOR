import numpy as np
from scipy.optimize import linprog
import heapq


def branch_and_bound(c, A, b, bounds):
    """
    Решение задачи целочисленного линейного программирования методом ветвей и границ.

    Параметры:
    - c: коэффициенты целевой функции (1D массив).
    - A: матрица ограничений (2D массив).
    - b: правая часть ограничений (1D массив).
    - bounds: список пар (min, max) для переменных (список кортежей).

    Возвращает:
    - Оптимальное значение целевой функции.
    - Оптимальный вектор решений (или None, если нет решения).
    """
    queue = []
    best_solution = None
    best_value = -np.inf

    res = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')
    #print("linprog status:", res.status)  # 2 - нет решений, 3 - неограниченная

    if res.success:
        heapq.heappush(queue, (-res.fun, res.x, A, b))  # Приоритет -res.fun для max heap

    while queue:
        _, x, current_A, current_b = heapq.heappop(queue)  # Извлекаем узел с наибольшим потенциалом
        res = linprog(c, A_ub=current_A, b_ub=current_b, bounds=bounds, method='highs')

        if np.all(x == np.floor(x)):
            value = -res.fun
            if value > best_value:
                best_value = value
                best_solution = x
            continue

        if res.fun <= best_value:
            continue

        fractional_index = np.argmax(x - np.floor(x))
        fractional_value = x[fractional_index]

        lower_A = np.vstack([current_A, np.zeros(len(c))])
        lower_A[-1, fractional_index] = 1  # x[fractional_index] <= floor(fractional_value)
        lower_b = np.append(current_b, np.floor(fractional_value))

        upper_A = np.vstack([current_A, np.zeros(len(c))])
        upper_A[-1, fractional_index] = -1  # x[fractional_index] >= ceil(fractional_value)
        upper_b = np.append(current_b, -np.ceil(fractional_value))

        for new_A, new_b in [(lower_A, lower_b), (upper_A, upper_b)]:
            res = linprog(c, A_ub=new_A, b_ub=new_b, bounds=bounds, method='highs')
            #print("linprog status:", res.status)  # 2 - нет решений, 3 - неограниченная
            if res.success:
                heapq.heappush(queue, (-res.fun, tuple(res.x), new_A, new_b))

    return best_value, best_solution
