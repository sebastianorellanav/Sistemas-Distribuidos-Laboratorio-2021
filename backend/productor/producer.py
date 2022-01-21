# Librerías
from kafka import KafkaProducer
import json
import requests
from time import sleep
from datetime import date, timedelta, datetime

# Constantes
TOPIC_NAME = 'terremoto'

# Función para conectarse a la API de terremotos
def get_earthquakes():
    param = {}
    today = date.today()
    yesterday = today - timedelta(days=1)
    today = today.strftime("%Y-%m-%d")
    yesterday = yesterday.strftime("%Y-%m-%d")
    param["starttime"] = yesterday
    param["endtime"] = today
    param["format"]="geojson"
    param["limit"]= 20000
    request_data= requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query",params=param)
    request_data=request_data.json()
    request_data=request_data["features"]
    respuesta=[]
    for x in request_data:
        add=x["properties"]
        add["id"]=x["id"]
        respuesta.append(add)
    return respuesta

# Se crear el productor
producer = KafkaProducer(bootstrap_servers='kafka:9093')

# Por siempre hacer:
while True: 
    sleep(60) # Esperar 60 segundo para hacer una nueva request
    # Obtener Terremotos
    response = get_earthquakes()
    timestamp = datetime.now()
    print("[", timestamp, "] - OTENIENDO TERREMOTOS")

    # Guardar terremotos en Kafka
    for terremoto in response:
        timestamp = datetime.now()
        print("[", timestamp, "] - GUARDANDO TERREMOTO CON ID= ", terremoto["id"])
        producer.send(TOPIC_NAME, json.dumps(terremoto).encode('utf-8'))
    
    





