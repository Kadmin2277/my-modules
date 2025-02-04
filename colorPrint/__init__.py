from colorPrint import Exception

class ColorPrint:
    COLORS = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
    }

    @staticmethod
    def colorPrint(text, color):
        if color not in ColorPrint.COLORS:
            raise Exception.ColorError(color)
        print(f"{ColorPrint.COLORS[color]}{text}{ColorPrint.COLORS['reset']}")