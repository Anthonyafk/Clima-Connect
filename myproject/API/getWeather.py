from flask import Flask, render_template, request
from API.config import OPENWEATHER_API_KEY
import requests
import difflib

app = Flask(__name__)

api_key = OPENWEATHER_API_KEY

nombres_abreviados = {
    "ciudad de méxico": ["ciudad de méxico", "mex", "cdmx"],
    "guadalajara": ["guadalajara", "gdl"],
    "cancun": ["cancun", "cun"],
    "tijuana": ["tijuana", "tij"],
    "puerto vallarta": ["puerto vallarta", "pvr"],
    "monterrey": ["monterrey", "mty"]
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
        ciudad = encontrar_nombre_similar(ciudad)
    
    url = f"http://api.openweathermap.org/data/2.5/weather?q={ciudad},{pais}&appid={api_key}"

    try:
        response = requests.get(url)
        response.raise_for_status()
        
        data = response.json()
        temperatura_celsius = data.get("main", {}).get("temp", 0) - 273.15
        return render_template("index.html", data=data, ciudad=ciudad, temperatura_celsius=temperatura_celsius)
    except requests.exceptions.RequestException as e:
        error_message = "Error al obtener datos del tiempo. Por favor, verifica tu conexión a Internet."
        return render_template("error.html", error_message=error_message)

if __name__ == "__main__":
    app.run(debug=True)

