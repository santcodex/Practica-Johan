import os
import sys

directorio_colab = '/content/drive/My Drive'
directorio_local = os.getcwd()

def montardrive():
   
    try:
        from google.colab import drive
        drive.mount('/content/drive')
        print("Google Drive montado con éxito.")
    except ImportError:
        print("Google Colab no detectado. Ejecutando en entorno local.")

def directorioactual():
    
    if "google.colab" in sys.modules:
        return directorio_colab
    else:
        return directorio_local

def listararchivos(directorio):
    
    try:
        archivos = sorted(os.listdir(directorio)) 
        print(f"Archivos en el directorio '{directorio}' (orden alfabético):")
        for archivo in archivos:
            print(archivo)
    except FileNotFoundError:
        print(f"Error: El directorio '{directorio}' no fue encontrado.")
    except PermissionError:
        print(f"Error: No se tienen permisos para acceder al directorio '{directorio}'.")

def main():
    
    if "google.colab" in sys.modules:
        montardrive()
    directorio = directorioactual()
    print(f"Directorio utilizado: {directorio}")
    listararchivos(directorio)

if __name__ == "__main__":
    main()
