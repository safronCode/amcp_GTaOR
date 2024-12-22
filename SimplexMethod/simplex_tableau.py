import numpy as np

def create_tableau(c, A, b, sign):
    """
        Создание симплекс-матрицы для задачи линейного программирования.
        Задача должна быть в форме Ax <= b для ограничений и max cx.

        c: коэффициенты целевой функции (1D numpy array).
        A: матрица ограничений (2D numpy array).
        b: правая часть ограничений (1D numpy array).
        sign: вектор (1D numpy array). 1: <= , 0: ==, -1: >=
    """

    num_vars = len(c)
    num_constraints = len(b)

    tableau = np.zeros((num_constraints + 1, num_vars + num_constraints + 1))
    tableau[:num_constraints, :num_vars] = A
    tableau[:num_constraints, -1] = b

    #todo вот тут заебись как будтобы
    reverse = sign < 0
    tableau[np.append(reverse, False)] *= -1


    tableau[:num_constraints, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    tableau[-1, :num_vars] = -c

    return tableau
