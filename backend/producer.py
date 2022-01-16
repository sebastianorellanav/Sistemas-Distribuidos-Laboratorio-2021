from kafka import KafkaProducer
import json

TOPIC_NAME = 'test'
msg = {
    "status": 200, 
    "message": "mensaje de prueba", 
    "terremotos": [1,2,3,4,"string"]
    }

#Crear el productor
producer = KafkaProducer(bootstrap_servers='localhost:9092')

#Enviar el mensaje 
producer.send(TOPIC_NAME, json.dumps(msg).encode('utf-8'))