class ColorError(Exception):
    def __init__(self, color):
        self.color = color
        super().__init__(f'Цвет "{self.color}" не найден.')