import csv

# Cargar el DataSet 1 en un diccionario (usaremos las coordenadas como clave)
dataset1 = {}
with open('dataset1.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        coords = (
            float(row['origin_latitude']),
            float(row['origin_longitude']),
            float(row['destination_latitude']),
            float(row['destination_longitude'])
        )
        dataset1[coords] = row

# Cargar el DataSet 2 en un diccionario (usaremos el número de boleto como clave)
dataset2 = {}
with open('dataset2.csv', mode='r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        ticket_number = row['num_ticket']
        dataset2[ticket_number] = row

# Función para buscar por número de boleto
def buscar_por_numero_de_boleto(numero_boleto):
    if numero_boleto in dataset2:
        return dataset2[numero_boleto]
    else:
        return None  # El número de boleto no se encontró en el DataSet 2

# Función para buscar por coordenadas
def buscar_por_coordenadas(latitud_origen, longitud_origen, latitud_destino, longitud_destino):
    coords = (latitud_origen, longitud_origen, latitud_destino, longitud_destino)
    if coords in dataset1:
        return dataset1[coords]
    else:
        return None  # Las coordenadas no se encontraron en el DataSet 1

# Crear un diccionario para mapear códigos IATA a ciudades
iata_a_ciudad = {
    "TLC": "Toluca",
    "MTY": "Monterrey",
    # Agrega otros mapeos de códigos IATA a ciudades aquí
}

# Función para obtener la ciudad de origen desde un código IATA
def obtener_ciudad_desde_iata(origin_iata):
    return origin_iata.get(origin_iata, "Ciudad Desconocida")  # Devuelve "Ciudad Desconocida" si no se encuentra el código IATA

# Ejemplo de uso:
numero_boleto = 'kw9f0kwvZJmsukQy'  # Cambia esto al número de boleto que deseas buscar
resultado_boleto = buscar_por_numero_de_boleto(numero_boleto)

if resultado_boleto:
    print(f"Resultado de búsqueda por número de boleto ({numero_boleto}):")
    print(resultado_boleto)
else:
    print(f"No se encontró ningún boleto con el número {numero_boleto}")

# Ejemplo de búsqueda por coordenadas (cambia las coordenadas según tus necesidades):
lat_origen = 19.3371
lon_origen = -99.566 
lat_destino = 25.7785
lon_destino = -100.107

resultado_coordenadas = buscar_por_coordenadas(lat_origen, lon_origen, lat_destino, lon_destino)

if resultado_coordenadas:
    print("\nResultado de búsqueda por coordenadas:")
    print(resultado_coordenadas)
else:
    print("\nNo se encontraron coincidencias para las coordenadas proporcionadas")
