from flask import render_template, request
from API.config import OPENWEATHER_API_KEY
import requests

api_key = OPENWEATHER_API_KEY

nombres_abreviados = {
    "ciudad de méxico": ["ciudad de méxico", "mex", "cdmx", "mxm"],
    "guadalajara": ["guadalajara", "gdl"],
    "cancun": ["cancun", "cun"],
    "tijuana": ["tijuana", "tij"],
    "puerto vallarta": ["puerto vallarta", "pvr"],
    "veracruz": ["veracruz", "ver", "acruz"],
    "monterrey": ["monterrey", "mty", "mon"]
}

def encontrar_nombre_similar(entrada_usuario):
    entrada_usuario = entrada_usuario.lower()
    
    for nombre, abreviaturas in nombres_abreviados.items():
        if entrada_usuario in abreviaturas:
            return nombre
    
    coincidencias = difflib.get_close_matches(entrada_usuario, nombres_abreviados.keys())
    
    if coincidencias:
        return coincidencias[0]
    else:
        return None

def obtener_datos_del_tiempo(ciudad="Tokyo" ):
    pais = "jp"
    
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