"""
Importa la función obtener_datos_del_tiempo desde el módulo clima.py.
"""
from API.getWeather import obtener_datos_del_tiempo

# Diccionario para los datos climáticos de ciudades
cache = {}

def obtener_datos_del_cache(ciudad):
    if ciudad in cache:
        # Si la ciudad está en el caché, devuelve los datos almacenados
        return cache[ciudad]
    else:
        # Si la ciudad no está en el caché, realiza la solicitud a la API y almacena los datos en caché
        data = obtener_datos_del_tiempo(ciudad)  # Aquí debes implementar tu función para obtener datos de la API
        cache[ciudad] = data  # Almacena los datos en caché
        return data






