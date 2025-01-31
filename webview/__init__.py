# pip install PyQt5 PyQtWebEngine
import os
try:
    from PyQt5.QtWidgets import QApplication, QMainWindow
    from PyQt5.QtWebEngineWidgets import QWebEngineView
except ImportError: os.system("pip install PyQt5 PyQrWebEngine")
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from webview import Exception

class WebView(QMainWindow):
    def __init__(self, url: str, title: str = "WebView"):
        super().__init__()
        self.setWindowTitle(title)
        self.setGeometry(100, 100, 800, 600)
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)

    def show_window(self):
        self.show()


def run_webview(url: str = "", title: str = "WebView"):
    if url == "":
        raise Exception.WebViewUrlNotFounded('The "url" field is empty. Enter your URL address in this field.')
    else:
        app = QApplication(sys.argv)
        window = WebView(url, title)
        window.show_window()
        sys.exit(app.exec_())