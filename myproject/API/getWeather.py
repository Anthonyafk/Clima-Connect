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
    
    if request.method == "POST":
        entrada = request.form.get("ciudad")
        
        # Verifica si la entrada contiene números, si es un ticket.
        if contiene_numeros(entrada):
            ciudad_abreviada = get_destination_by_ticket(entrada)
            ciudad = encontrar_nombre_similar(ciudad_abreviada)
        else:
           ciudad = encontrar_nombre_similar(entrada)
    
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


