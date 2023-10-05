"""
Imports
Importamos las bibliotecas necesarias para nuestra aplicación Flask.
"""
from flask import Flask, render_template, request
from API.getWeather import obtener_datos_del_tiempo

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Definición de la ruta principal ("/") y métodos permitidos (GET y POST)
@app.route("/", methods=["GET", "POST"])
def main():
    """
    Función principal de la aplicación Flask.
    Se encarga de manejar las solicitudes GET y POST a la ruta principal ("/").
    """
    if request.method == "POST":
        ciudad = request.form.get("ciudad")  # Obtener la ciudad desde el formulario web
        ciudad = obtener_datos_del_tiempo(ciudad)

        return f"{ciudad}"  # Mostrar la ciudad en la página web

    return render_template("index.html")