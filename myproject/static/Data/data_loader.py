"""
Importamos la biblioteca csv para trabajar con archivos CSV.
"""
import csv

# Ruta al archivo CSV que contiene los datos.
csv_file_path = r'Coloca aqui tu direccion de codigo'

# Diccionario que almacenará los datos del archivo CSV.
data = {}

# Leer el archivo CSV y almacenar los datos en el diccionario 'data'.
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
    Obtiene el origen basado en el número de ticket proporcionado.
    
    Entrada:
        num_ticket (str): El número de ticket para el cual se desea obtener el origen.
    
    Salida:
        str: El origen asociado con el número de ticket.
        None: Si el número de ticket no se encuentra en los datos.
    """
    if num_ticket in data:
        return data[num_ticket]['origin']
    else:
        return None

def obtener_ticket_de_destino(num_ticket):
    """
    Obtiene el destino basado en el número de ticket proporcionado.
    
    Entrada:
        num_ticket (str): El número de ticket para el cual se desea obtener el destino.
    
    Salida:
        str: El destino asociado con el número de ticket.
        None: Si el número de ticket no se encuentra en los datos.
    """
    if num_ticket in data:
        return data[num_ticket]['destination']
    else:
        return None




