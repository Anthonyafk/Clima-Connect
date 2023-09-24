from flask import Flask, render_template, request
from API.config import OPENWEATHER_API_KEY
import requests
from utils.SintaxisErrorsbyUser import encontrar_nombre_similar
from Data.data_loader import get_origin_by_ticket, get_destination_by_ticket

app = Flask(__name__)

api_key = OPENWEATHER_API_KEY

def contiene_numeros(texto):
    return any(char.isdigit() for char in texto)

def obtener_datos_del_tiempo(ciudad="Cuernavaca" ):
    pais = "mx"
    ciudad_origen = ""
    origen = ""  # Inicializa origen con una cadena vacía
    ciudad_destino = ""  # Inicializa ciudad_destino con una cadena vacía
    pais = request.form.get("pais")
    
    if request.method == "POST":
        entrada = request.form.get("ciudad")
        
        # Verifica si la entrada contiene números, si es un ticket.
        if contiene_numeros(entrada):
            ciudad_abreviada = get_destination_by_ticket(entrada)
            ciudad = encontrar_nombre_similar(ciudad_abreviada)
            origen = get_origin_by_ticket(entrada)
            ciudad_origen = encontrar_nombre_similar(origen)  # Obtén la ciudad de origen
            ciudad_destino = encontrar_nombre_similar(origen)  # Asigna el mismo valor a ciudad_destino si es apropiado
        else:
           ciudad = encontrar_nombre_similar(entrada)
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"
    url_origen = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad_origen},{pais}&appid={api_key}"  # Obtén el clima de la ciudad de origen

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        temperatura_celsius = data.get("main", {}).get("temp", 0) - 273.15
        
        # Obtén los datos del clima de la ciudad de origen
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
    
if __name__ == "__main__":
    app.run(debug=True)