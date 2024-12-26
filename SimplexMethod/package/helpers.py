import matplotlib.pyplot as plt
import numpy as np


path2mpc = 'C:\\your_path_to_project\\...'

def color_print(string, color: str):
    colors = {
        'RED':'\033[31m\033[21m',
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m\033[21m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m\033[26m',
        'RESET': '\033[0m'
    }

    # Получаем код цвета из словаря или устанавливаем сброс по умолчанию
    color_code = colors.get(color.upper(), colors['RESET'])
    print(f"{color_code}{string}{colors['RESET']}")

def plot_comparasion1(x,y1,y2):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label="highs (scipy)", color="blue", linewidth=3, marker='o')
    plt.plot(x, y2, label="simplex method (amcp)", color="coral", linewidth=3, marker='o')

    plt.title("Сравнение временных затрат относительно кол-ва переменных бенчмарка", fontsize=14)
    plt.xlabel('Количество переменных в бенчмарке')
    plt.ylabel('Затрачено секунд')

    plt.grid(True, linewidth=1)
    plt.legend(fontsize=12)
    plt.yscale("log")
    plt.show()


def plot_comparasion2(b_name, iteration, values_simplex, value_highs, value_exact):
    iter = np.linspace(0, iteration, iteration+1)
    values_highs = np.full((1, iteration+1), value_highs).ravel()
    values_exact = np.full((1, iteration+1), value_exact).ravel()
    plt.figure(figsize=(8, 6))
    plt.figure(figsize=(8, 6))
    plt.plot(iter, values_simplex, label="Simplex", color="coral", linewidth=3, marker='o')
    plt.plot(iter, values_highs, label="Highs", color="blue",linestyle='--', linewidth=2)
    plt.plot(iter, values_exact, label="exact", color="green",linestyle='--', linewidth=2)
    plt.title(f"Бенчмарк {b_name}: Пошаговая сходимость", fontsize=14)
    plt.xlabel('Количество итераций')
    plt.ylabel('Значение целевой функции')
    plt.grid(True, linewidth=1)
    plt.legend(fontsize=12)
    plt.show()


