"""
AJCZ Web Agency - Desktop App v6
Con animación de entrada al iniciar
"""

import sys
from datetime import datetime
from pathlib import Path
from urllib.parse import quote

from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QFont, QPalette, QColor, QDesktopServices
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView

WHATSAPP_NUMBER = "18298511786"
WHATSAPP_MESSAGE = "Hola AJCZ, me interesa hablar sobre un proyecto web."

WHATSAPP_URL = f"https://wa.me/{WHATSAPP_NUMBER}?text={quote(WHATSAPP_MESSAGE)}"

WINDOW_TITLE = "AJCZ - Agencia de Diseño Web"
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900

CURRENT_YEAR = str(datetime.now().year)

APP_DIR = Path(__file__).resolve().parent
HTML_TEMPLATE_PATH = APP_DIR / "ajcz_animacion.html"


def _whatsapp_opens_in_system_browser(url: QUrl) -> bool:
    """Enlaces de WhatsApp deben abrirse fuera del WebView (wa.me no sirve bien embebido)."""
    if url.scheme() not in ("http", "https"):
        return False
    host = url.host().lower()
    return host in ("wa.me", "www.wa.me") or host.endswith(
        ("whatsapp.com", "whatsapp.net")
    )


class WhatsAppWebPage(QWebEnginePage):
    """Abre wa.me y dominios de WhatsApp en el navegador predeterminado del SO."""

    def acceptNavigationRequest(self, url, _type, is_main_frame):
        if _whatsapp_opens_in_system_browser(url):
            QDesktopServices.openUrl(url)
            return False
        return super().acceptNavigationRequest(url, _type, is_main_frame)

    def createWindow(self, wtype):
        # Enlaces con target="_blank" abren una ventana nueva en el motor; la capturamos aquí.
        popup = QWebEnginePage(self.profile(), self)

        def on_url_changed(url):
            if url.isValid() and _whatsapp_opens_in_system_browser(url):
                QDesktopServices.openUrl(url)
                popup.deleteLater()

        popup.urlChanged.connect(on_url_changed)
        return popup


def load_html_template() -> str:
    """
    Carga la plantilla HTML desde disco y reemplaza placeholders básicos.
    Si la plantilla no existe, devuelve un mensaje HTML mínimo de error.
    """
    if not HTML_TEMPLATE_PATH.exists():
        return f"""<!DOCTYPE html>
<html lang="es">
<head><meta charset="UTF-8"><title>{WINDOW_TITLE}</title></head>
<body style="background:#050d1a;color:#ccd6f6;font-family:Arial, sans-serif;display:flex;align-items:center;justify-content:center;min-height:100vh;">
  <div style="max-width:600px;text-align:center;">
    <h1>Plantilla no encontrada</h1>
    <p>No se encontró el archivo <code>{HTML_TEMPLATE_PATH.name}</code> en el directorio de la aplicación.</p>
  </div>
</body>
</html>"""

    html = HTML_TEMPLATE_PATH.read_text(encoding="utf-8")
    html = html.replace("{{WHATSAPP_URL}}", WHATSAPP_URL)
    html = html.replace("{{YEAR}}", CURRENT_YEAR)
    return html


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(WINDOW_TITLE)
        self.setGeometry(100, 100, WINDOW_WIDTH, WINDOW_HEIGHT)
        
        self.web_view = QWebEngineView()
        self.web_view.setPage(
            WhatsAppWebPage(self.web_view.page().profile(), self.web_view)
        )
        html = load_html_template()
        base_url = QUrl.fromLocalFile(str(APP_DIR / ""))
        self.web_view.setHtml(html, base_url)
        
        self.setCentralWidget(self.web_view)
        
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor(5, 13, 26))
        self.setPalette(palette)
        self.setStyleSheet("background-color: #050d1a;")


def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    font = QFont("DM Sans", 10)
    app.setFont(font)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
