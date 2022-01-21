# Librerías
from kafka import KafkaConsumer
from json import loads
from datetime import datetime
from time import sleep
import psycopg2

# Constantes
TOPIC_NAME = 'terremoto'

sleep(20) # Esperar 30 segundos antes de crear el consumidor

timestamp = datetime.now()
print("[", timestamp, "] - CREANDO CONSUMIDOR ...")
consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=['kafka:9093'],auto_offset_reset='earliest',enable_auto_commit=True,value_deserializer=lambda x: loads(x.decode('utf-8')))

timestamp = datetime.now()
print("[", timestamp, "] - CONECTANDO CON BASES DE DATOS POSTGRESQL ...")
conn = psycopg2.connect( database="terremotos", user='postgres', password='postgres', host='db', port= '5432')
cursor = conn.cursor()

#Leer los mensajes
while True:
    sleep(10)
    timestamp = datetime.now()
    print("[", timestamp, "] - CONSUMIENDO TERREMOTOS DESDE KAFKA ...")
    for terremoto in consumer:
        terremoto = terremoto.value
        try:
            cursor.execute("INSERT INTO terremoto (id,mag,place,time,updated,tz,url,detail,felt,cdi,mmi,alert,status,tsunami,sig,net,code,ids,sources,types,nst,dmin,rms,gap,mag_type,tipe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(terremoto["id"],terremoto["mag"],terremoto["place"],terremoto["time"],terremoto["updated"],terremoto["tz"],terremoto["url"],terremoto["detail"],terremoto["felt"],terremoto["cdi"],terremoto["mmi"],terremoto["alert"],terremoto["status"],terremoto["tsunami"],terremoto["sig"],terremoto["net"],terremoto["code"],terremoto["ids"],terremoto["sources"],terremoto["types"],terremoto["nst"],terremoto["dmin"],terremoto["rms"],terremoto["gap"],terremoto["magType"],terremoto["type"]))
            conn.commit()
            timestamp = datetime.now()
            print("[", timestamp, "] - GUARDANDO TERREMOTO CON ID= ", terremoto["id"], " EN BASE DE DATOS")
        except Exception as e:
            timestamp = datetime.now()
            print("[", timestamp, "] - EL TERREMOTO CON ID= ", terremoto["id"], " YA FUE GUARDADO EN LA BASE DE DATOS")
            conn.rollback()
    conn.close()