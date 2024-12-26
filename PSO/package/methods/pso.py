from PSO.package.params import *
from typing import Callable

def pso(function: Callable):
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
    fit = function(x)
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
        fit = function(x)

        # Обновление pbest
        better_fit = fit < pbest_val
        pbest_val[better_fit] = fit[better_fit]
        pbest[:, better_fit] = x[:, better_fit]

        # Обновление gbest
        ind = np.argmin(pbest_val)
        gbest_val[iter] = np.copy(pbest_val[ind])
        gbest = np.copy(pbest[:, ind])
        gbest_store[:, iter] = np.copy(gbest)
        #print("Iter. =", iter, ". gbest_val = ", gbest_val[iter]) ##Situationally

        x_store[iter, :, :] = x
        #print("gbest_point = ", gbest) #Situationally
    return iter, gbest_val, gbest, [gbest_store, x_store]
