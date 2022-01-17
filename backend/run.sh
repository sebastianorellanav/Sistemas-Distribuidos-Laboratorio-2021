#!/bin/bash

exec python3 consumer.py &
exec python3 producer.py &
exec flask db upgrade &
exec python3 -m flask run &
echo SERVICIOS PYTHON INICIALIZADOS
