# Importa la función desde clima.py
from clima import obtener_datos_del_tiempo

# Diccionario para los datos climáticos de ciudades
datos_climaticos = {}

def obtener_datos_ciudad(ciudad):
    """
    Obtiene los datos climáticos de una ciudad dada.

    Args:
        ciudad (str): El nombre de la ciudad.

    Returns:
        dict: Un diccionario con los datos climáticos de la ciudad o None si la ciudad no existe en los datos.
    """
    # Comprueba si los datos climáticos ya están en el diccionario
    if ciudad in datos_climaticos:
        return datos_climaticos[ciudad]

    # Si los datos no están en el diccionario, realiza una consulta a la API y almacena los resultados
    # Esto es solo un ejemplo, debes adaptarlo a tu código de consulta real a la API
    datos_ciudad = obtener_datos_del_tiempo(ciudad)

    # Almacena los datos en el diccionario
    datos_climaticos[ciudad] = datos_ciudad

    return datos_ciudad


