import os
import shutil
import sys

EXTENSIONES = {
    ".pdf": "PDF",
    ".jpg": "Imagenes",
    ".jpeg": "Imagenes",
    ".png": "Imagenes",
    ".docx": "Word",
    ".xlsx": "Excel",
    ".mp3": "Audio",
    ".zip": "Comprimidos",
}

if len(sys.argv) < 2:
    print("Uso: python organizador.py <ruta_carpeta>")
    sys.exit(1)

ruta = sys.argv[1]

for archivo in os.listdir(ruta):
    ruta_archivo = os.path.join(ruta, archivo)
    if not os.path.isfile(ruta_archivo):
        continue

    _, extension = os.path.splitext(archivo)
    extension = extension.lower()

    carpeta = EXTENSIONES.get(extension)
    if carpeta is None:
        continue

    ruta_carpeta = os.path.join(ruta, carpeta)
    if not os.path.exists(ruta_carpeta):
        os.makedirs(ruta_carpeta)

    shutil.move(ruta_archivo, os.path.join(ruta_carpeta, archivo))
