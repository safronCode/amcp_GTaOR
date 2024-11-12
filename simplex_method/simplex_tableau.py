import numpy as np

def create_tableau(z, A, b):
    """
    Создание симплекс-матрицы для задачи линейного программирования.
    Задача должна быть в форме Ax <= b для ограничений и max cx.

    c: коэффициенты целевой функции (1D numpy array).
    A: матрица ограничений (2D numpy array).
    b: правая часть ограничений (1D numpy array).
    """

    num_vars = len(z)
    num_constraints = len(b)

    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))

    tableau[:num_constraints, :num_vars] = A
    tableau[:num_constraints, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    tableau[:num_constraints, -1] = b

    tableau[-1, :num_vars] = -z
    return tableau
