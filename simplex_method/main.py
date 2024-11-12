from simplex_method import *
from visualization import color_print

"""
    SET INITIAL CONDITIONS

    F(X) = sum(zX)
    AX <= b
    
    :np.array z: Вектор строка
    :np.array A: Матрaица размерности len(b) x len(z)
    :np.array b: Вектор строка    
    :bool flag: Флаг для определния задачи минимизации/максимизации (по умолчанию максимизация)
                True <--> maximization
                False <--> minimization
"""

z = np.array([-6, -5])   # -6x_1 + -5x_2
                         # Наложенные ограничения
A = np.array([[7, 3],    # 7x_1 + 3x_2 <= 1365
              [6, 3],    # ...
              [1, 2],
              [-1, 0]])

b = np.array([1365, 1245, 650, -140])
flag = False


if __name__ == "__main__":
    point, func_value = simplex_method(z, A, b, flag)

    #Небольшой навал красивого вывода
    func_string = 'F(X) = '
    for i in range(len(z)):
        func_string += str(z[i]) + f'x_{i + 1}'
        if i < len(z) - 1:
            func_string += ' + '

    # colors: GREEN, YELLOW, BLUE, MAGENTA, CYAN
    if flag:
        color_print(f'При заданых условиях {func_string} --> max:', 'BLUE')
    else:
        color_print(f'При заданых условиях {func_string} --> min:', 'BLUE')

    formatted_point = [f"{val:.2f}" for val in point]
    print(f' В точке x*: {formatted_point}\n F(x*) = {func_value:.2f}')
