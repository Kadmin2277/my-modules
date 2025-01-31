class ExecutorNotImported(BaseException):
    """Исключение для того чтоб пользователь импортировал файл executor.py"""

def package(package: str):
    package = package

def main():
    raise ExecutorNotImported("Для работы данного модуля используйте доп. файл executor")

if __name__ == '__main__':
    main()