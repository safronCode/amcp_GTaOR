from simplex_method import *
from visualization import color_print

""" 
    color_print -> colors: RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN
    
    SET INITIAL CONDITIONS

    F(X) = sum(zX)
    AX <= b
    
    :np.array z: Вектор строка
    :np.array A: Матрица размерности len(b) x len(z)
    :np.array b: Вектор строка    
    :bool flag: Флаг для определения задачи минимизации/максимизации (по умолчанию максимизация)
                True <--> maximization
                False <--> minimization
"""

c = np.array([2, -2])

A = np.array([[1, 0],
              [0, 6/4],
              [6/3.5, 0],
              [1,1]])

b = np.array([4.5, 6, 6, 1])

sign = np.array ([1, 1, 1, -1])

if __name__ == "__main__":

    func_string = 'F(X) = '
    for i in range(len(c)):
        func_string += str(c[i]) + f'x_{i + 1}'
        if i < len(c) - 1:
            func_string += ' + '

    for mode in [1,-1]:
        point, fval = simplex_method(mode * c, A, b, sign)
        formatted_point = [f"{val:.2f}" for val in point]

        if mode == 1:
            color_print(f'При заданных условиях {func_string} --> maximization:', 'RED')
            print(f' В точке x*: {formatted_point}\n F(x*) = {fval:.2f}')

        else:
            color_print(f'При заданных условиях {func_string} --> minimization:', 'BLUE')
            print(f' В точке x*: {formatted_point}\n F(x*) = {-fval:.2f}')
