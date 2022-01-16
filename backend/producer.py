from kafka import KafkaProducer
import json
import requests
from time import sleep
from datetime import date, timedelta

TOPIC_NAME = 'terremoto'
#msg = {
#    "status": 200, 
#    "message": "mensaje de prueba", 
#    "terremotos": [1,2,3,4,"string"]
#    }

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

#Crear el productor
producer = KafkaProducer(bootstrap_servers='localhost:9092')

for i in range(120): #60 Minutes
    print("nuevo ciclo en el for")
    headers = {
        'Client-Identifier': 'dan-citymonitor',
    }

    response = get_earthquakes()
    #r = response.json()
    #Enviar el mensaje 
    producer.send(TOPIC_NAME, json.dumps(response).encode('utf-8'))
    print("antes del sleep")
    sleep(30)





