from kafka import KafkaConsumer
from json import loads
from datetime import datetime
from time import sleep
import psycopg2
TOPIC_NAME = 'terremoto'
#Crear el consumidor
print("consumidor")
consumer = KafkaConsumer(TOPIC_NAME,bootstrap_servers=['kafka:9092'],auto_offset_reset='earliest',enable_auto_commit=True,group_id='my-group',value_deserializer=lambda x: loads(x.decode('utf-8')))
print("conectando a psycopg2")
conn = psycopg2.connect( database="terremotos", user='postgres', password='postgres', host='db', port= '5432')
print("tomando cursor")
cursor = conn.cursor()
print("entrando a while")
#Leer los mensajes
while True:
    print("reintentando",consumer,cursor)
    sleep(20)
    for message in consumer:
        print("\n\nVALUE:",message.value)
        message = message.value
        for terremoto in message:
            print("\n\nTERREMOTO:",terremoto)
            try:
                cursor.execute("INSERT INTO terremoto (id,mag,place,time,updated,tz,url,detail,felt,cdi,mmi,alert,status,tsunami,sig,net,code,ids,sources,types,nst,dmin,rms,gap,mag_type,tipe) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(terremoto["id"],terremoto["mag"],terremoto["place"],terremoto["time"],terremoto["updated"],terremoto["tz"],terremoto["url"],terremoto["detail"],terremoto["felt"],terremoto["cdi"],terremoto["mmi"],terremoto["alert"],terremoto["status"],terremoto["tsunami"],terremoto["sig"],terremoto["net"],terremoto["code"],terremoto["ids"],terremoto["sources"],terremoto["types"],terremoto["nst"],terremoto["dmin"],terremoto["rms"],terremoto["gap"],terremoto["magType"],terremoto["type"]))
                conn.commit()
                print("terremoto agregado: ",terremoto["id"])
            except Exception as e:
                print("no fue agregado con error",e,'\n\n')
                conn.rollback()
conn.close()