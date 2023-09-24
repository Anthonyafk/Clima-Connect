# Imports
from flask import Flask, render_template, request
from API.getWeather import obtener_datos_del_tiempo


# para runnear la app
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        ciudad = request.form.get("ciudad")  # Obtener la ciudad desde el formulario web
        ciudad = obtener_datos_del_tiempo(ciudad)

        return f"{ciudad}"  # Mostrar la ciudad en la página web

    return render_template("index.html")
