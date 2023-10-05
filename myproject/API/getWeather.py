"""
Importaciones necesarias para la aplicación Flask.
"""
from flask import Flask, render_template, request, jsonify
from API.config import OPENWEATHER_API_KEY
import requests
from utils.SintaxisErrorsbyUser import encontrar_nombre_similar
from Data.data_loader import obtener_ticket_de_origen, obtener_ticket_de_destino

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Clave de la API de OpenWeatherMap
api_key = OPENWEATHER_API_KEY

# Función auxiliar para verificar si una cadena contiene números
def contiene_numeros(texto):
    return any(char.isdigit() for char in texto)

# Ruta principal ("/") y métodos permitidos (GET y POST)
@app.route("/", methods=["GET", "POST"])
def obtener_datos_del_tiempo(ciudad="Cuernavaca"):
    """
    Función que obtiene y muestra los datos climáticos de una ciudad.

    Args:
        ciudad (str): El nombre de la ciudad.

    Returns:
        render_template: Una plantilla HTML que muestra los datos climáticos o un mensaje de error.
    """
    pais = "mx"
    ciudad_origen = ""
    origen = ""  # Inicializa origen con una cadena vacía
    ciudad_destino = ""  # Inicializa ciudad_destino con una cadena vacía
    pais = request.form.get("pais")

    
    
    if request.method == "POST":
        entrada = request.form.get("ciudad")
 
        
        # Verifica si la entrada contiene números, si es un ticket.
    if contiene_numeros(entrada):
            ciudad_abreviada = obtener_ticket_de_destino(entrada)
            ciudad = encontrar_nombre_similar(ciudad_abreviada)
            origen = obtener_ticket_de_origen(entrada)
            ciudad_origen = encontrar_nombre_similar(origen)  # Obtiene la ciudad de origen
            ciudad_destino = encontrar_nombre_similar(origen)  # Asigna el mismo valor a ciudad_destino si es apropiado
    else:
           ciudad = encontrar_nombre_similar(entrada)
           
    if ciudad is None:
            error_message = "Nombre de ciudad o ticket inválido. Recargue la página e inténtelo otra vez."
            return render_template("error.html", error_message=error_message)
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"
    url_origen = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad_origen},{pais}&appid={api_key}"  # Obtén el clima de la ciudad de origen

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        temperatura_celsius = data.get("main", {}).get("temp", 0) - 273.15
        
        # Obtiene los datos del clima de la ciudad de origen
        response_origen = requests.get(url_origen)
        response_origen.raise_for_status()
        data_origen = response_origen.json()
        temperatura_celsius_origen = data_origen.get("main", {}).get("temp", 0) - 273.15
        humedad_origen = data_origen.get("main", {}).get("humidity", 0)
        descripcion_origen = data_origen['weather'][0]['description']
        presion_origen = data_origen.get("main", {}).get("pressure", 0)
        
        return render_template("index.html", data=data, ciudad=ciudad, temperatura_celsius=temperatura_celsius, origen=origen, temperatura_celsius_origen=temperatura_celsius_origen, humedad_origen=humedad_origen, descripcion_origen=descripcion_origen, presion_origen=presion_origen, ciudad_destino=ciudad_destino, encontrar_nombre_similar=encontrar_nombre_similar)
    except requests.exceptions.RequestException as e:
        error_message = "Error al obtener datos del tiempo. Por favor, verifica tu conexión a Internet."
        return render_template("error.html", error_message=error_message)

# Nueva ruta para manejar la solicitud AJAX de obtención de datos climáticos
@app.route("/obtener_datos_climaticos", methods=["POST"])
def obtener_datos_climaticos():
    ciudad = request.form.get("ciudad")
    datos_clima = obtener_datos_del_tiempo(ciudad)  # Llama a tu función para obtener datos climáticos

    # Asegúrate de tener una variable 'descripcion' en 'datos_clima' que contenga la descripción del clima
    if "descripcion" in datos_clima:
        return jsonify(datos_clima)
    else:
        return jsonify({"error": "No se pudieron obtener los datos climáticos"})

# Comprueba si se está ejecutando el archivo directamente
if __name__ == "__main__":
    app.run(debug=True)

