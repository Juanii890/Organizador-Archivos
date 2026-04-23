import os
import shutil

ruta = "C:/Users/TuUsuario/Downloads"

for archivo in os.listdir(ruta):
    if archivo.endswith(".pdf"):
        carpeta = "PDF"
    elif archivo.endswith(".jpg") or archivo.endswith(".png"):
        carpeta = "Imagenes"
    else:
        continue

    if not os.path.exists(os.path.join(ruta, carpeta)):
        os.makedirs(os.path.join(ruta, carpeta))

    shutil.move(os.path.join(ruta, archivo), os.path.join(ruta, carpeta, archivo))
