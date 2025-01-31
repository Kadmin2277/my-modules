import os

DOWNLOADED = False

try:
    import execjs
except ImportError:
    global DOWNLOADED
    DOWNLOADED = True
    os.system("python3 -m pip install PyExecJS")


class JSExecutor:
    def __init__(self):
        self.context = execjs.compile('''function runJS(code) { return eval(code); }''')

    def innerJS(self, js_code: str):
        """Выполнить JavaScript-код."""
        try:
            result = self.context.call("runJS", js_code)
            print(result)
        except Exception as e:
            print(f"Error executing JavaScript: {e}")

    def getJSFile(self, file_path: str):
        """Выполнить JavaScript-код из файла."""
        try:
            with open(file_path, 'r') as file:
                js_code = file.read()
            self.innerJS(js_code)
        except FileNotFoundError:
            print(f"File not found: {file_path}")

    def setHTML(self, html_content: str):
        """Установить HTML-содержимое."""
        with open('output.html', 'w') as file:
            file.write(html_content)
        print("HTML content saved to output.html")

    def templateHTML(self, file_path: str):
        """Установить HTML-содержимое из файла."""
        try:
            with open(file_path, 'r') as file:
                html_content = file.read()
            self.setHTML(html_content)
        except FileNotFoundError:
            print(f"File not found: {file_path}")