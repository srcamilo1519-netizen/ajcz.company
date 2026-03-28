#!/usr/bin/env python3
"""
AJCZ Build Script - PyInstaller
Compila la aplicación a ejecutable standalone
"""

import subprocess
import sys
import shutil
from pathlib import Path

def build():
    """Compila la aplicación con PyInstaller"""
    
    print("🚀 Iniciando build de AJCZ...")
    
    # Verificar que existe el HTML template
    if not Path("ajcz_animacion.html").exists():
        print("❌ Error: No se encontró ajcz_animacion.html")
        sys.exit(1)
    
    # Comando PyInstaller
    cmd = [
        sys.executable, "-m", "PyInstaller",
        "--name=AJCZ-Web-Agency",
        "--onefile",
        "--windowed",
        "--add-data=ajcz_animacion.html:.",
        "--clean",
        "--noconfirm",
        "ajcz_animacion.py"
    ]
    
    print("📦 Ejecutando PyInstaller...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode == 0:
        print("✅ Build completado exitosamente!")
        print("📁 Ejecutable generado en: dist/AJCZ-Web-Agency.exe")
        
        # Limpiar carpetas temporales
        if Path("build").exists():
            shutil.rmtree("build")
        
        # Info adicional
        exe_path = Path("dist/AJCZ-Web-Agency.exe")
        if exe_path.exists():
            size_mb = exe_path.stat().st_size / (1024 * 1024)
            print(f"📊 Tamaño del ejecutable: {size_mb:.1f} MB")
    else:
        print("❌ Error en el build:")
        print(result.stderr)
        sys.exit(1)

if __name__ == "__main__":
    build()
