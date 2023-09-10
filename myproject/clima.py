
# Imports
from flask import Flask, render_template, request
from API.getWeather import obtener_datos_del_tiempo, encontrar_nombre_similar


# para runnear la app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        ciudad = request.form.get("ciudad")  # Obtener la ciudad desde el formulario web

        # Corregir el nombre de la ciudad si es necesario
        ciudad_corregida = encontrar_nombre_similar(ciudad)
        
        ciudad = ciudad_corregida  # Establecer la ciudad corregida como la ciudad de búsqueda

        # Llama a obtener_datos_del_tiempo() y almacena la ciudad obtenida
        ciudad = obtener_datos_del_tiempo(ciudad)

        return f"{ciudad}"  # Mostrar la ciudad en la página web

    return render_template("index.html")

