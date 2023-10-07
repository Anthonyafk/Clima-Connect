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

2. Establecer la variable de entorno:

### Para windows:

Haz clic en el icono de Windows o pulsa la tecla Win en tu teclado.

Escribe "cmd" o "símbolo del sistema".

En los resultados, haz clic derecho en "Símbolo del sistema" y selecciona "Ejecutar como administrador".

En algunos casos aparecerá un cuadro de diálogo de Control de cuentas de usuario (UAC) pidiéndote permiso para permitir que la aplicación realice cambios en tu dispositivo. Haz clic en "Sí" para continuar.

Usa el siguiente comando: 

```
setx OPENWEATHER_API_KEY "36a510e66cf5393e1e5e2e70c2aad861" /M
```

Cierra y vuelve a abrir la línea de comandos para que los cambios surtan efecto.

### Para Linux:

Presione Ctrl+Alt+T y pegue lo siguiente en la terminal:

```
export OPENWEATHER_API_KEY="36a510e66cf5393e1e5e2e70c2aad861

```

3. Navegue hasta la carpeta en la que se instalo su repositorio y despues entre en Clima-connect:

```
cd Clima-Connect/

```
4. Instale los demas paquetes del programa (aqui se incluye flask):

```
pip install -r requirements.txt

```

5. Coloca la dirrecion del archivo dataset2 en data_loader.py:

En el archivo llamado data_loader.py que esta dentro de la carpeta Data que a su vez esta dentro de la carperta static se tiene que cambiar la direccion de memoria del archivo del dataset2 el cual tambien se encuentra en la carpeta Data. Si no sabes como escribir esta dirreccion aqui hay un pequeño tutorial

### Para Windonws:
Busca la carpta de proyecto (Clima-Connect) despues entra a la carpeta "myproject" despues entra a la carpeta "static" y al ultimo a la carpeta "Data" busca el archivo llamado "dataset2.csv" y presiona click izquierdo sobre el, despues escoje la opccion "propiedades" y aparecera una pantalla en la cual habra varios datos del archivo, el que nos intereza es el que diga "ubicacion" ahi debera aparecerte algo parecido a esto: 

- "C:\Users\danie\Downloads\Clima-Connect\myproject\static\Data"

copia ese texto y pegalo en un bloc de notas, ahora añade despues de "\Data"  lo siguiente: "\dataset2.csv" la direccion del archivo deberia quedarte algo asi: 

- ***C:\Users\danie\Downloads\Clima-Connect\myproject\static\Data\dataset2.csv***

- ***/home/above37845/Documents/Modelado y Programación/Clima-Connect/myproject/static/Data/dataset2.csv***


###Para Linux:

Ahora abre el archivo data_loader.py y encuentra donde dice: 

***csv_file_path = r'Coloca aqui tu direccion de codigo'***

Sin quitar las comillas simples borra el texto y pega la direccion del archivo dataset2, guarda los cambios y listo

6. Navegue hasta myProject

```
cd myproject

```

7. Cree su entorno virtual 

Para Linux:

```
python3 -m venv .venv

```

Para Windows:

```
py -3 -m venv .venv

```
6. Active su entorno virtual

Para Linux:

```
. .venv/bin/activate

```

Para Windows:
```
.venv\Scripts\activate

```
7. Runne la app

```
flask --app clima run 

```
