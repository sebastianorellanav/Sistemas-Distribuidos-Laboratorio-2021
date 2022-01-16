from kafka import KafkaConsumer

TOPIC_NAME = 'test'

#Crear el consumidor
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=['localhost:9092'])

#Leer los mensajes
for message in consumer:
    # message value and key are raw bytes -- decode if necessary!
    # e.g., for unicode: `message.value.decode('utf-8')`
    print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))