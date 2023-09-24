"""
Importamos la biblioteca csv para trabajar con archivos CSV.
"""
import csv

# Obtiene la ruta completa al archivo CSV (reemplaza 'Tu direccion del archivo dataset2.csv' con la ubicación real del archivo)
csv_file_path = r'"Tu direccion del archivo dataset2.csv por ejemplo: C:\Users\danie\Downloads\Proyecto-1 - copia\myproject\Data\dataset2.csv"'

# Carga los datos del archivo CSV en un diccionario
data = {}
with open(csv_file_path, mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        data[row['num_ticket']] = {
            'origin': row['origin'],
            'destination': row['destination'],
            'origin_latitude': float(row['origin_latitude']),
            'origin_longitude': float(row['origin_longitude']),
            'destination_latitude': float(row['destination_latitude']),
            'destination_longitude': float(row['destination_longitude'])
        }

def obtener_ticket_de_origen(num_ticket):
    """
    Función que obtiene el origen asociado a un número de boleto (num_ticket).

    Args:
        num_ticket (str): El número de boleto para buscar el origen.

    Returns:
        str: El nombre del origen correspondiente al num_ticket o None si no se encuentra en los datos.
    """
    if num_ticket in data:
        return data[num_ticket]['origin']
    else:
        return None  # Devuelve None si el num_ticket no se encuentra en los datos

def obtener_ticket_de_destino(num_ticket):
    """
    Función que obtiene el destino asociado a un número de boleto (num_ticket).

    Args:
        num_ticket (str): El número de boleto para buscar el destino.

    Returns:
        str: El nombre del destino correspondiente al num_ticket o None si no se encuentra en los datos.
    """
    if num_ticket in data:
        return data[num_ticket]['destination']
    else:
        return None  # Devuelve None si el num_ticket no se encuentra en los datos



