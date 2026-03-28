#!/usr/bin/env python3
"""
Crear GitHub Release para AJCZ Web Agency
Sube el instalador completo como asset
"""

import os
import sys
import json
import requests
from pathlib import Path

# Configuración
REPO = "srcamilo1519-netizen/ajcz.company"
TOKEN = "github_pat_11A2O4X3Y0X8XqXqXqXqXq_1234567890abcdef"  # Reemplazar con tu token real

def create_release():
    """Crear release y subir archivo"""
    
    # Leer archivo del instalador
    installer_path = "../AJCZ-Web-Agency-Installer.zip"
    if not os.path.exists(installer_path):
        print(f"Error: No se encuentra {installer_path}")
        return False
    
    # Datos del release
    release_data = {
        "tag_name": "v1.0.0",
        "name": "AJCZ Web Agency v1.0.0",
        "body": """# AJCZ Web Agency v1.0.0

## 📦 Paquete de Instalación Completo

Este release contiene el instalador completo para AJCZ Web Agency.

### 📁 Contenido del ZIP:
- `AJCZ-Web-Agency.exe` - Aplicación principal (194 MB)
- `install.bat` - Instalador automático
- `icon.ico` - Icono profesional
- `README.txt` - Instrucciones completas

### 🚀 Instalación:
1. Descargar `AJCZ-Web-Agency-Installer.zip`
2. Descomprimir
3. Ejecutar `install.bat` como administrador
4. Listo ✅

### ✅ Características:
- ✅ Instalación automática
- ✅ Sin dependencias
- ✅ Compatible con Windows 10/11
- ✅ Portable (USB)

---
© 2026 AJCZ Web Agency
""",
        "draft": False,
        "prerelease": False
    }
    
    # Crear release
    headers = {
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json"
    }
    
    print("Creando release...")
    response = requests.post(
        f"https://api.github.com/repos/{REPO}/releases",
        headers=headers,
        json=release_data
    )
    
    if response.status_code != 201:
        print(f"Error creando release: {response.status_code}")
        print(response.text)
        return False
    
    release = response.json()
    upload_url = release["upload_url"].replace("{?name,label}", "")
    release_id = release["id"]
    
    print(f"Release creado: #{release_id}")
    
    # Subir archivo
    print(f"Subiendo {installer_path}...")
    
    with open(installer_path, "rb") as f:
        files = {
            "file": (os.path.basename(installer_path), f, "application/zip")
        }
        headers = {
            "Authorization": f"token {TOKEN}",
            "Content-Type": "application/zip"
        }
        
        upload_response = requests.post(
            upload_url,
            headers=headers,
            files=files
        )
    
    if upload_response.status_code != 201:
        print(f"Error subiendo archivo: {upload_response.status_code}")
        print(upload_response.text)
        return False
    
    asset = upload_response.json()
    download_url = asset["browser_download_url"]
    
    print(f"✅ Release completo!")
    print(f"📦 Download URL: {download_url}")
    
    # Guardar URLs
    with open("release_info.json", "w") as f:
        json.dump({
            "release_id": release_id,
            "download_url": download_url,
            "tag_name": "v1.0.0"
        }, f, indent=2)
    
    return True

if __name__ == "__main__":
    if create_release():
        print("✅ Release creado exitosamente")
    else:
        print("❌ Error creando release")
        sys.exit(1)
