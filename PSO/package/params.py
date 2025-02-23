import numpy as np

'''Параметры управления PSO (м. роя)'''
w = 0.5  # Вес инерции
c1 = 2.0  # Локальная компонента
c2 = 2.0  # Глобальная компонента
v_fct = 0.02

Np = 60  # Число частиц
D = 2  # Размерность пространства
max_iter = 200  # Число итераций
xL = np.zeros(D) - 10  # Нижняя граница пространства
xU = np.zeros(D) + 10  # Верхняя граница пространства