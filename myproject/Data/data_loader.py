import csv

def cargar_dataset(nombre_archivo):
    """
    Carga los datos del dataset desde un archivo CSV y los convierte en un diccionario.

    Args:
        nombre_archivo (str): El nombre del archivo CSV que contiene los datos.

    Returns:
        dict: Un diccionario con los datos del dataset.
    """
    datos_dataset = {}
    with open(nombre_archivo, newline='') as archivo_csv:
        lector_csv = csv.DictReader(archivo_csv)
        for fila in lector_csv:
            origin = fila['Ciudad de Origen']
            destination = fila['Ciudad de Destino']
            datos_ciudad = {
                'origin_latitude': float(fila['Origen Latitud']),
                'origin_longitude': float(fila['Origen Longitud']),
                'destination_latitude': float(fila['Destino Latitud']),
                'destination_longitude': float(fila['Destino Longitud']),
            }
            datos_dataset[f'{origin} - {destination}'] = datos_ciudad  # Usamos una clave única para cada ciudad

    return datos_dataset

# Cargar el dataset y convertirlo en un diccionario
ciudades_dataset = cargar_dataset('dataset1.csv')