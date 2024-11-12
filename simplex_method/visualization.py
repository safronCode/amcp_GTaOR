def color_print(string, color: str):
    colors = {
        'GREEN': '\033[32m',
        'YELLOW': '\033[33m',
        'BLUE': '\033[34m',
        'MAGENTA': '\033[35m',
        'CYAN': '\033[36m',
        'RESET': '\033[0m'
    }

    # Получаем код цвета из словаря или устанавливаем сброс по умолчанию
    color_code = colors.get(color.upper(), colors['RESET'])
    print(f"{color_code}{string}{colors['RESET']}")
