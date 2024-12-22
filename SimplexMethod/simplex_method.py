import numpy as np
from SimplexMethod.simplex_tableau import create_tableau

def simplex_method (c, A, b,sign, mode='max'):
    # Создаём симплекс таблицу (в задача лп в канон. форме)
    tableau = create_tableau(c,A,b,sign)

    basis = np.arange(len(c) + 1 , len(c) + 1 + len(b))
    point = np.zeros(len(c) + len(b))

    while np.any(tableau[-1] < 0):
        # Выбираем индекс где наименьший, из тех, что < 0
        columnIndex = np.argmin(tableau[-1])
        pivotColumn = tableau[:, columnIndex]

        extraColumn = np.where(tableau[:-1, columnIndex] == 0, np.nan, (tableau[:-1, -1] / pivotColumn[:-1]))
        extraColumn[extraColumn <= 0] = np.nan

        if np.all(np.isnan(extraColumn)):
            print("Фунционал не достигает экстремума в заданной области")
            return 0

        rowIndex = np.nanargmin(extraColumn)

        basis[rowIndex] = columnIndex+1
        tableau[rowIndex] = tableau[rowIndex] / tableau[rowIndex, columnIndex]

        # todo подумать над этим шагом мб через свойства матриц можно как-то
        for i in range(0, tableau.shape[0]):
            if i == rowIndex:
                pass
            else:
                tableau[i] = tableau[i] - (tableau[i, columnIndex] * tableau[rowIndex])

        for j in range(0, A.shape[0]):
            point[basis[j]-1] = tableau[j, -1]

    return point[0:c.shape[0]],tableau[-1,-1]
