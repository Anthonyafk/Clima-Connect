import subprocess
import sys
import venv

def crear_entorno_virtual():
    try:
        venv.create(".venv", with_pip=True)
    except Exception as e:
        print(f"Error al crear el entorno virtual: {e}")
        sys.exit(1)

def instalar_dependencias():
    try:
        subprocess.check_call([".venv/bin/pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error al instalar dependencias: {e}")
        sys.exit(1)

def configuracion_inicial():
    # metodo extra para conf inicial
    pass

def main():
    print("Configurando el proyecto...")
    crear_entorno_virtual()
    instalar_dependencias()
    configuracion_inicial()
    print("Configuración completa. Ahora puedes ejecutar la aplicación.")

if __name__ == "__main__":
    main()
