from flask import render_template, request
from API.config import OPENWEATHER_API_KEY
import requests

api_key = OPENWEATHER_API_KEY

# Función principal para obtener los datos del tiempo desde la API
def obtener_datos_del_tiempo(ciudad="Tokyo" ): # Ciudad predeterminada
    pais = "jp" # Pais por defecto
    
    if request.method == "POST":
        ciudad = request.form.get("ciudad")
        pais = request.form.get("pais")
    
    # URL de la API de OpenWeatherMap con ciudad y país
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()
        
        # Realiza la conversión de grados Kelvin a grados Celsius
        temperatura_celsius = data.get("main", {}).get("temp", 0) - 273.15
        
        # Muestra los datos del tiempo en la página
        return render_template("index.html", data=data, ciudad=ciudad, temperatura_celsius=temperatura_celsius)
    except requests.exceptions.RequestException as e:
        return f"Error al obtener datos del tiempo: {e}"