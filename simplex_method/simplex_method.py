import numpy as np
from simplex_tableau import create_tableau

def simplex_method(z, A, b, flag=True):

    tableau = create_tableau(z, A, b)
    iter_cnt = 0
    basis = np.arange(len(z)+1, len(z)+1+len(b))

    # TODO Переработать флаг, мб вообще на$%! выкинуть его
    if flag:

    # TODO придумать другую конструкцию (не while) - мб получится сократить O(N)
        # Задача максимизации
        while np.any(tableau[-1] < 0):
            iter_cnt += 1
            idx = np.where(tableau[-1] < 0)[0][0]

            pivot_column = np.where(tableau[:-1, idx] <= 0, np.inf, tableau[:-1, -1] / tableau[:-1, idx])

            idx2 = np.argmin(pivot_column)
            basis[idx2] = idx + 1

            tableau[idx2] = tableau[idx2]/tableau[idx2,idx]

            #todo подправить for
            for i in range (0, tableau.shape[0]):
                if i == idx2:
                    pass
                else:
                    tableau[i] = tableau[i] - (tableau[i,idx] * tableau[idx2])


        point = np.zeros(len(z)+len(b))

        for j in range(0, A.shape[0]):
            point[basis[j]-1] = tableau[j, -1]


        funct = 0

        #todo уверен можно скоратить через numpy. (см np.dot)
        for k in range(0, len(z)):
            funct += z[k] * point[k]

        #return tableau , basis , iter_cnt
        return point[0:len(z)] , funct


    else:
        # Задача минимизации
        while np.any(tableau[-1] > 0):
            iter_cnt += 1
            idx = np.where(tableau[-1] > 0)[0][0]


            pivot_column = np.where(tableau[:-1, idx] == 0, np.inf, tableau[:-1, -1] / tableau[:-1, idx])

            idx2 = np.argmin(pivot_column)  # !!! почему третья итерация тут min 0 а не 1
            basis[idx2] = idx + 1

            tableau[idx2] = tableau[idx2] / tableau[idx2, idx]

            # todo подправить for
            for i in range(0, tableau.shape[0]):
                if i == idx2:
                    pass
                else:
                    tableau[i] = tableau[i] - (tableau[i, idx] * tableau[idx2])

        point = np.zeros(len(z) + len(b))

        for j in range(0, A.shape[0]):
            point[basis[j] - 1] = tableau[j, -1]

        funct = 0

        # todo уверен можно скоратить через numpy. (см np.dot)
        for k in range(0, len(z)):
            funct += z[k] * point[k]

        # return tableau , basis , iter_cnt
        return point[0:len(z)], funct