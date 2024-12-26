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

    reverse = sign < 0
    tableau[np.append(reverse, False)] *= -1


    tableau[:num_constraints, num_vars:num_vars + num_constraints] = np.eye(num_constraints)
    tableau[-1, :num_vars] = -c

    return tableau

def simplex_method(c, A, b, sign):
    """
        Реализация симплекс-метода для задачи линейного программирования.

        c: коэффициенты целевой функции (1D numpy array).
        A: матрица ограничений (2D numpy array).
        b: правая часть ограничений (1D numpy array).
        sign: вектор (1D numpy array).
    """
    iteration = 0
    iter_fval = np.array([0])

    tableau = create_tableau(c, A, b, sign)

    basis = np.arange(len(c) + 1, len(c) + 1 + len(b))
    point = np.zeros(len(c) + len(b))

    while np.any(tableau[-1, :-1] < 0):
        columnIndex = np.argmin(tableau[-1, :-1])
        pivotColumn = tableau[:-1, columnIndex]


        ratios = np.divide(
            tableau[:-1, -1],
            pivotColumn,
            out=np.full_like(tableau[:-1, -1], np.inf),
            where=pivotColumn > 0
        )

        if np.all(np.isinf(ratios)):
            print("\033[21mФункционал не достигает экстремума в заданной области\033[0m")
            return None, None, None


        rowIndex = np.argmin(ratios)

        basis[rowIndex] = columnIndex + 1

        tableau[rowIndex, :] /= tableau[rowIndex, columnIndex]

        for i in range(tableau.shape[0]):
            if i != rowIndex:
                tableau[i, :] -= tableau[i, columnIndex] * tableau[rowIndex, :]
        iteration += 1

        iter_fval = np.concatenate((iter_fval, [-tableau[-1, -1]]), axis=0)

    for i in range(len(basis)):
        point[basis[i] - 1] = tableau[i, -1]

    return point[:len(c)], -tableau[-1, -1], [iteration, iter_fval]
