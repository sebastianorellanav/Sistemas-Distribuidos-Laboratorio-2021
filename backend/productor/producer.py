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
producer = KafkaProducer(bootstrap_servers='kafka:9093')
sleep(20)
while True: #60 Minutes
    print("nuevo ciclo en el for")

    response = get_earthquakes()
    
    for terremoto in response:
        print("se estan enviando las cosas a kafka")
        producer.send(TOPIC_NAME, json.dumps(terremoto).encode('utf-8'))
        print("antes del sleep")
    
    sleep(60)





