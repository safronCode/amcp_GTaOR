import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

# Параметры управления PSO
w = 0.5  # Вес инерции
c1 = 2.0  # Локальная компонента
c2 = 2.0  # Глобальная компонента
v_fct = 0.02

Np = 60  # Число частиц
D = 2  # Размерность пространства
max_iter = 200  # Число итераций
xL = np.zeros(D) - 15  # Нижняя граница пространства
xU = np.zeros(D) + 15  # Верхняя граница пространства

# Функция Шоффера (Schaffer Function N. 4)
def function_Schaffer_n4(x):
    return 0.5 + (np.cos(np.sin(np.abs(x[0]**2 - x[1]**2)))**2 - 0.5) / (1 + 0.001 * (x[0]**2 + x[1]**2))**2

# Создание сетки для визуализации
delta = 0.1
xplt = yplt = np.arange(xL[0], xU[0], delta)
X, Y = np.meshgrid(xplt, yplt)
Z = function_Schaffer_n4([X, Y])

# Инициализация PSO
pbest_val = np.zeros(Np)  # Лучшая фитнес-оценка каждой частицы
gbest_val = np.zeros(max_iter)  # Лучшая глобальная фитнес-оценка на каждой итерации
pbest = np.zeros((D, Np))  # Лучшая позиция каждой частицы
gbest = np.zeros(D)  # Глобально лучшая позиция
gbest_store = np.zeros((D, max_iter))  # Хранение лучших позиций
x = np.random.rand(D, Np)  # Начальная позиция частиц
v = np.zeros((D, Np))  # Начальная скорость частиц
x_store = np.zeros((max_iter, D, Np))  # Хранение позиций для анимации

# Установка начальных позиций частиц
for m in range(D):
    x[m, :] = xL[m] + (xU[m] - xL[m]) * x[m, :]

# Оценка фитнес-функции для начальных позиций
fit = function_Schaffer_n4(x)
pbest_val = np.copy(fit)
pbest = np.copy(x)

# Инициализация глобального оптимума
ind = np.argmin(pbest_val)
gbest_val[0] = np.copy(pbest_val[ind])
gbest = np.copy(pbest[:, ind])
x_store[0, :, :] = x

# PSO Итерации
for iter in range(1, max_iter):
    r1 = np.random.rand(D, Np)
    r2 = np.random.rand(D, Np)
    v_global = c2 * r2 * (gbest.reshape(-1, 1) - x)
    v_local = c1 * r1 * (pbest - x)
    v = w * v + v_local + v_global
    x = x + v * v_fct
    fit = function_Schaffer_n4(x)

    # Обновление pbest
    better_fit = fit < pbest_val
    pbest_val[better_fit] = fit[better_fit]
    pbest[:, better_fit] = x[:, better_fit]

    # Обновление gbest
    ind = np.argmin(pbest_val)
    gbest_val[iter] = np.copy(pbest_val[ind])
    gbest = np.copy(pbest[:, ind])
    gbest_store[:, iter] = np.copy(gbest)
    print("Iter. =", iter, ". gbest_val = ", gbest_val[iter])

    x_store[iter, :, :] = x
    print("gbest_point = ", gbest)

# Анимация
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(xL[0], xU[0])
ax.set_ylim(xL[1], xU[1])
ax.set_xlabel('x')
ax.set_ylabel('y')

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
ani.save('pso_schaffer_animation.gif', fps=20)
#plt.show()
