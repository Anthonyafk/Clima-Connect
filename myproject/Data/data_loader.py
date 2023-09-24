import csv

# Obtén la ruta completa al archivo CSV

csv_file_path = '/home/above37845/Documents/Modelado y Programación/Clima-Connect/myproject/Data/dataset2.csv'

# Cargar los datos del archivo CSV en un diccionario
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

# Función para obtener el origen dado un num_ticket
def get_origin_by_ticket(num_ticket):
    if num_ticket in data:
        return data[num_ticket]['origin']
    else:
        return None  # Devuelve None si el num_ticket no se encuentra en los datos

# Función para obtener el destino dado un num_ticket
def get_destination_by_ticket(num_ticket):
    if num_ticket in data:
        return data[num_ticket]['destination']
    else:

        return None  # Devuelve None si el num_ticket no se encuentra en los datos
