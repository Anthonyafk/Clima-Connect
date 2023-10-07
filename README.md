Integrantes:

* Antonio Castillo Hernández          No. de Cuenta: 320017438 

* Francisco Daniel García López       No. de Cuenta: 320104321

## Introducción:

# Clima Connect

Clima Connect es una aplicación web que te permite obtener el pronóstico del clima para una ciudad o ingresar un "ticket" relacionado con una ciudad de destino.

## Funcionalidades

- Consulta el pronóstico del clima actual para una ciudad específica.
- Ingresa un "ticket" para obtener el pronóstico del clima de tu ciudad de destino y también muestra información de la ciudad de origen. De igual forma admite nombres de ciudades tanto bien escritas como mal escritas.

## Tecnologías Utilizadas

- Python
- Flask (Framework web)
- HTML
- CSS
- API de Pronóstico del Tiempo (para obtener datos del clima)


## Prerrequisitos

Antes de ejecutar esta aplicación, asegúrate de cumplir con los siguientes requisitos:

1. **Python**: Asegúrate de tener Python instalado en tu computadora. Si no lo tienes, puedes descargarlo desde el [sitio web oficial de Python](https://www.python.org/downloads/).

2. **pip (Administrador de Paquetes de Python)**: Verifica que tengas `pip` instalado. Pip generalmente se instala automáticamente con Python, pero puedes verificar su existencia ejecutando el siguiente comando en tu terminal o símbolo del sistema:

## Configuración del Proyecto

1. Clona este repositorio en tu máquina local:

```bash
git clone https://github.com/Anthonyafk/Clima-Connect.git

```
2. Navegue hasta la carpeta en la que se instalo su repositorio y despues entre en Clima-connect:

```
cd Clima-Connect/

```
3. Instale los demas paquetes del programa:

```
pip install -r requirements.txt

```

4. Ejecute el Setup:

```
python setup.py

```
5. Navegue hasta myProject

```
cd myproject

```

6. Ejecute 

```
flask --app clima run 

```

En dado caso de que surjan problemas haga lo sig:

**(solamente navegue hasta donde tiene instalado su repo)**
```
cd Downloads\Clima-Connect
```
**(cree un entorno virtual)**
```
python3 -m venv .venv
```
**(activelo con ese comando)**
```
. .venv/bin/activate
```
**(si no lo tiene instalado escriba ese comando)**
```
pip install Flask
```
**(si no lo tiene instalado escriba ese comando)**
```
pip install requests
```
**(regrese a myproject)**
```
cd myproject
```
**(runne la app)**
```
flask --app clima run 
```

**Disclaimer:**
En el archivo llamado dataLoader.py que esta dentro de la carpeta Data se tiene que cambiar la direccion de memoria del archivo del dataSet dependiendo de donde se te haya instalado. es decir en:

```
csv_file_path = r'/home/above37845/Documents/Modelado y Programación/Clima-Connect/myproject/Data/dataset2.csv'

```

Lo que esta entre parentecis: '/home/above37845/Documents/Modelado y Programación/Clima-Connect/myproject/Data/dataset2.csv' debera cambiarse por la dirección en la que este ese archivo en tu dispositivo.
