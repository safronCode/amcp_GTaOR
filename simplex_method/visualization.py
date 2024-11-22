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
