import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from statistics import mode
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
import modelos as mo
db= mo.objeto_db()
app= Flask(__name__)
CORS(app)


app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/terremotos"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

ma = Marshmallow(app)
migrate= Migrate(app,db)



def get_info(param):
	
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

def stats(data):
	estadisticas={
		"mag":[0,0,0],
		"sig":[0,0,0],
		"gap":[0,0,0],
		"rms":[0,0,0]
	}
	
	df=pd.DataFrame(data)
	if not df.empty:
		for i in [0,13,20,21,22]:
			columna=df.columns[i]
			df[columna]=pd.to_numeric(df[columna])
			promedio=df[columna].mean()
			mediana=df[columna].median()
			moda=mode(df[columna].tolist())	
			estadisticas[columna]=[promedio,mediana,moda]

	return estadisticas


@app.route("/terremotos",methods=["GET"])
def api_consumer():
	
	argumentos=request.args.to_dict()
	datos=get_info(argumentos)
	
	estadisticas=stats(datos)
	retornar={"terremotos":datos,"estadisticas": estadisticas}
	return jsonify(retornar)




"""
@app.route("/terremotos/estadisticas",methods=["GET"])
def stats():
	parametros={}
	datos=get_info(parametros)
	
	totales=0
	tsunamis=0
	grado=0
	alertas=[0,0,0,0,0]
	for x in datos:
		if x["mag"] != None:
			grado+=x["mag"]
			if x["tsunami"]==1:
				tsunamis+=1
			totales+=1
	
	tsunamis=(tsunamis*100)/totales
	grado=(grado)/totales
	
	datos={
		"totales":totales,
		"terremoto_con_prob_tsunami":tsunamis,
		"grado_promedio":grado
		

	}
	
	return jsonify(datos)
"""
@app.route("/terremotos/<pais>",methods=["GET"])
def paises(pais):
	parametros={}
	resultado=[]
	print(pais)
	datos=get_info(parametros)
	
	for x in datos:
		if x["place"]!=None:
			lugar=x["place"].split(',')[-1]
			if lugar[0]==' ':
				lugar=lugar[1:]
			if lugar == pais:
				resultado.append(x)
	estadisticas=stats(resultado)
	retornar={"terremotos":resultado,"estadisticas": estadisticas}
	return jsonify(retornar)


if __name__ == '__main__':
	app.run(debug=True)
