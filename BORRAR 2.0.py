import os
import glob
import shutil
import subprocess

def borrar_archivos_carpetas(ruta):
    try:
        if os.path.isfile(ruta):
            os.remove(ruta)
            return True
        elif os.path.isdir(ruta):
            shutil.rmtree(ruta)
            return True
    except Exception as e:
        return False

def main():
    carpetas = [
        os.path.join(os.environ.get('TEMP'), '*'),
        os.path.join(os.environ.get('SystemRoot'), 'Prefetch', '*'),
        os.path.join(os.environ.get('TEMP'), '*')  # Para %TEMP%
    ]

    for carpeta in carpetas:
        archivos_carpeta = glob.glob(carpeta)  # Usamos glob.glob() para obtener la lista de archivos
        for archivo_carpeta in archivos_carpeta:
            if borrar_archivos_carpetas(archivo_carpeta):
                print(f"Archivo eliminado: {archivo_carpeta}")
            else:
                print(f"No se pudo eliminar el archivo: {archivo_carpeta}")

if __name__ == "__main__":
    main()
