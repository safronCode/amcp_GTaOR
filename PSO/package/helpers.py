from .params import *
import matplotlib.pyplot as plt
from matplotlib import animation


'''
    Cодержание helpers:
    * Функция Шаффера №4
    * Точные значения глобально оптимального решения (https://ru.wikipedia.org/wiki/Тестовые_функции_для_оптимизации)
    * Графики для отображения сходимости к точным значения относительно итераций алгоритма
    * Анимация работы PSO
'''

# Точные значения
true_min_val = 0.292579
true_min_point = (1.25313, 0)

# Функция двух переменных
def function_Schaffer_n4(x):
    return 0.5 + (np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2


# График сходимости значения функции
def plot_fval_convergence(gbest_val):
    plt.figure(figsize=(8, 6))
    plt.plot(gbest_val, label="Процесс оптимизации")
    plt.axhline(y=true_min_val, color='r', linestyle='--', label="Истинное значение минимума")
    plt.xlabel('Итерации')
    plt.ylabel('Значение функции')
    plt.legend()
    plt.title("Сходимость значения функции")
    plt.savefig("images/pso_fval_convergence.png")
    plt.show()


# График сходимости переменной x[0]
def plot_var_convergence(gbest_store, order:int):
    plt.figure()
    plt.plot(gbest_store[order, :], label=f"Траектория x[{order}]", linewidth=3)
    plt.axhline(y=true_min_point[order], color='r', linestyle='--', label=f"Истинное значение x[{order}]", linewidth=2)
    plt.axhline(y=-true_min_point[order], color='r', linestyle='--', label=f"Истинное значение -x[{order}]", linewidth=2)
    plt.xlabel('Итерации')
    plt.ylabel(f'Значение x[{order}]')
    plt.legend()
    plt.title(f'Сходимость переменной x[{order}]')
    plt.grid()
    plt.savefig(f"images/pso_val{order}_convergence.png")
    plt.show()

def animation_convergence(x_store, gbest_store):
    #Создание сетки визуализации
    delta = 0.1
    xplt = yplt = np.arange(xL[0], xU[0], delta)
    X, Y = np.meshgrid(xplt, yplt)
    Z = function_Schaffer_n4([X, Y])

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_xlim(xL[0], xU[0])
    ax.set_ylim(xL[1], xU[1])
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('Работа алгоритма PSO на примере Schaffer func. №4')

    contour = ax.contourf(X, Y, Z, levels=40, cmap='plasma')
    fig.colorbar(contour)
    line1, = ax.plot([], [], 'bo', markersize=3, label="Particles")
    line2, = ax.plot([], [], 'r*', markersize=12, label="Global Best")
    time_template = 'Iteration = {}'
    time_text = ax.text(0.05, 0.95, '', transform=ax.transAxes, color='white')
    ax.legend()

    # Инициализация анимации
    def init():
        line1.set_data([], [])
        line2.set_data([], [])
        time_text.set_text('')
        return line1, line2, time_text

    # Обновление анимации
    def animate(i):
        line1.set_data(x_store[i, 0, :], x_store[i, 1, :])
        line2.set_data([gbest_store[0, i]], [gbest_store[1, i]])  # Приведение к правильным размерам
        time_text.set_text(time_template.format(i))
        return line1, line2, time_text

    ani = animation.FuncAnimation(fig, animate, init_func=init, frames=max_iter, interval=50, blit=True)
    ani.save('images/pso_schaffer_animation.gif', fps=20)
    plt.show()
