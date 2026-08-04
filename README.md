# Organizador de Archivos

Script en Python que organiza automáticamente los archivos de una carpeta, moviéndolos a subcarpetas según su tipo (PDF, imágenes, Word, Excel, audio, comprimidos, etc.).

Pensado para automatizar una tarea manual y repetitiva: ordenar carpetas que se llenan de archivos sueltos (Descargas, Escritorio, carpetas de trabajo).

## Antes / después

**Antes:**
```
Descargas/
├── factura.pdf
├── foto.png
├── informe.docx
├── datos.xlsx
├── cancion.mp3
└── notas.txt
```

**Después de correr el script:**
```
Descargas/
├── PDF/
│   └── factura.pdf
├── Imagenes/
│   └── foto.png
├── Word/
│   └── informe.docx
├── Excel/
│   └── datos.xlsx
├── Audio/
│   └── cancion.mp3
└── notas.txt          <- se queda igual, extensión no reconocida
```

## Cómo usarlo

Requiere Python 3 (no necesita instalar librerías extra, solo usa el estándar de Python).

```bash
python organizador.py <ruta_de_la_carpeta>
```

Ejemplo real:

```bash
python organizador.py C:/Users/TuUsuario/Downloads
```

Si no le pasás una carpeta, el script te avisa cómo usarlo en vez de romperse:

```
Uso: python organizador.py <ruta_carpeta>
```

## Tipos de archivo que reconoce

| Extensión | Carpeta destino |
|---|---|
| .pdf | PDF |
| .jpg / .jpeg / .png | Imagenes |
| .docx | Word |
| .xlsx | Excel |
| .mp3 | Audio |
| .zip | Comprimidos |

Los archivos con extensiones no incluidas en esta lista se dejan sin tocar.

## Cómo agregar un tipo de archivo nuevo

Todo el mapeo vive en un diccionario al principio del script, así que agregar un tipo nuevo es una sola línea, sin tocar el resto de la lógica:

```python
EXTENSIONES = {
    ".pdf": "PDF",
    ".mp4": "Videos",  # <- nueva línea, así de simple
}
```

## Funcionalidades

- Clasificación automática de archivos por extensión (sin distinguir mayúsculas/minúsculas).
- Creación automática de las subcarpetas de destino si no existen.
- Ignora carpetas existentes dentro del directorio (no intenta mover carpetas como si fueran archivos).
- Extensible: sumar un tipo de archivo nuevo no requiere tocar la lógica del script.

## Tecnologías

- Python 3 (librerías estándar: `os`, `shutil`, `sys`)
