# AJCZ — Landing Page Animada + Aplicación de Escritorio

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=flat-square&logo=python)](https://python.org)
[![PyQt6](https://img.shields.io/badge/PyQt6-6.7%2B-green?style=flat-square&logo=qt)](https://riverbankcomputing.com/software/pyqt/)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey?style=flat-square)]()

> 🚀 **Agencia de Diseño Web Profesional** — Presentación interactiva con animaciones premium y aplicación de escritorio PyQt6.

![Preview](https://img.shields.io/badge/🎨-Cyberpunk%20Theme-64ffda?style=for-the-badge)

---

## ✨ Características

| Feature | Descripción |
|---------|-------------|
| 🎭 **Preloader Animado** | Animación de entrada con logo, línea expansiva y partículas flotantes |
| 🌐 **WebView Integrado** | Navegador embebido con PyQt6 WebEngine |
| 📱 **WhatsApp Directo** | Botón de contacto que abre WhatsApp Web o app nativa |
| 🎨 **Diseño Cyberpunk** | Paleta oscura con acentos cyan (#64ffda) |
| ⚡ **Animaciones CSS** | Transiciones suaves, hover effects, scroll reveals |
| 🖥️ **App de Escritorio** | Ejecutable multiplataforma con PyInstaller |

---

## 📁 Estructura del Proyecto

```
ajczzz-main/
├── ajcz_animacion.html      # Landing page con animaciones
├── ajcz_animacion.py        # Aplicación PyQt6 desktop
├── requirements.txt         # Dependencias Python
├── build.py                 # Script de compilación PyInstaller
├── README.md               # Este archivo
├── LICENSE                 # MIT License
└── CHANGELOG.md            # Historial de cambios
```

---

## 🚀 Instalación Rápida

### Requisitos Previos
- Python 3.9 o superior
- pip (gestor de paquetes Python)

### 1. Clonar o descargar
```bash
cd ajczzz-main
```

### 2. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 3. Ejecutar aplicación
```bash
python ajcz_animacion.py
```

---

## 📦 Compilar a Ejecutable

Para distribuir como app independiente (sin necesidad de Python instalado):

```bash
# Compilar para Windows
python build.py

# El ejecutable se generará en:
# dist/AJCZ-Web-Agency.exe
```

**Opciones del build script:**
- `--onefile` : Ejecutable único
- `--windowed` : Sin consola de fondo
- `--icon` : Incluye icono personalizado

---

## 🎨 Personalización

### Cambiar número de WhatsApp
Edita `ajcz_animacion.py` línea 17:
```python
WHATSAPP_NUMBER = "18298511786"  # Tu número aquí
WHATSAPP_MESSAGE = "Tu mensaje personalizado"
```

### Modificar colores del tema
Edita las variables CSS en `ajcz_animacion.html`:
```css
:root {
  --cyan: #64ffda;        /* Color primario */
  --bg: #050d1a;          /* Fondo oscuro */
  --card: #0b1e30;        /* Tarjetas */
}
```

### Ajustar tamaño de ventana
En `ajcz_animacion.py`:
```python
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 900
```

---

## 🛠️ Tecnologías Utilizadas

- **Frontend**: HTML5, CSS3 (animaciones CSS puras)
- **Backend/Desktop**: Python 3, PyQt6, PyQt6-WebEngine
- **Build**: PyInstaller
- **Fonts**: Syne, DM Sans (Google Fonts)

---

## 📋 Roadmap

- [x] Animación de preloader
- [x] Integración WhatsApp
- [x] Scroll reveal animations
- [x] PyInstaller build script
- [ ] Soporte para modo oscuro/claro toggle
- [ ] Multilenguaje (ES/EN)
- [ ] Formulario de contacto backend
- [ ] Analytics integrado

---

## 🤝 Contribuir

1. Fork el repositorio
2. Crea tu feature branch (`git checkout -b feature/nueva-funcion`)
3. Commit tus cambios (`git commit -am 'Añadir nueva función'`)
4. Push a la branch (`git push origin feature/nueva-funcion`)
5. Abre un Pull Request

---

## 📞 Contacto

- **WhatsApp**: [+1 (829) 851-1786](https://wa.me/18298511786)
- **Email**: ajczzz@gmail.com
- **Ubicación**: Santo Domingo, República Dominicana

---

## 📄 Licencia

Este proyecto está licenciado bajo la [MIT License](LICENSE) - ver archivo para detalles.

---

<p align="center">
  <sub>Hecho con 💚 y mucho código por <strong>AJCZ</strong></sub>
</p>
