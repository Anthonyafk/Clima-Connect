from flask import Flask, render_template, request
import requests
import difflib

app = Flask(__name__)

# Tu clave de API de OpenWeatherMap (reemplaza 'TU_API_KEY' con tu clave)
api_key = '36a510e66cf5393e1e5e2e70c2aad861'

# Lista de nombres conocidos y sus IATA code en minúsculas
nombres_abreviados = {
    "mexico city": ["ciudad de méxico", "mex", "cdmx"],
    "guadalajara": ["guadalajara", "gdl"],
    "cancun": ["cancun", "cun"],
    "tijuana": ["tijuana", "tij"],
    "puerto vallarta": ["puerto vallarta", "pvr"],
    "monterrey": ["monterrey", "mty"]
}

# Función para encontrar el nombre más cercano
def encontrar_nombre_similar(entrada_usuario):
    entrada_usuario = entrada_usuario.lower()  # Convertir a minúsculas
    
    for nombre, abreviaturas in nombres_abreviados.items():
        if entrada_usuario in abreviaturas:
            return nombre
    
    coincidencias = difflib.get_close_matches(entrada_usuario, nombres_abreviados.keys())
    
    if coincidencias:
        return coincidencias[0]
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def obtener_datos_del_tiempo():
    ciudad = "Tokyo"  # Ciudad predeterminada
    pais = "jp" # Pais por defecto
    
    if request.method == "POST":
        entrada_ciudad = request.form.get("ciudad")
        entrada_pais = request.form.get("pais")
        
        # Utiliza la función para encontrar el nombre similar
        nombre_similar = encontrar_nombre_similar(entrada_ciudad)
        
        if nombre_similar:
            ciudad = nombre_similar
            pais = entrada_pais
    
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

if __name__ == "__main__":
    app.run(debug=True)

