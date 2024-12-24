import matplotlib.pyplot as plt

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

def plot_comparasion(x,y1,y2):
    plt.figure(figsize=(8, 6))
    plt.plot(x, y1, label="highs (scipy)", color="blue", linewidth=3, marker='o')
    plt.plot(x, y2, label="simplex method (amcp)", color="coral", linewidth=3, marker='o')

    plt.title("Экспоненциальные кривые", fontsize=14)
    plt.xlabel('Количество переменных в бенчмарке')
    plt.ylabel('Затрачено секунд')

    plt.grid(True, linewidth=1)
    plt.legend(fontsize=12)
    plt.yscale("log")
    plt.show()

path2mpc = 'C:\\your_path_to_project\\...'