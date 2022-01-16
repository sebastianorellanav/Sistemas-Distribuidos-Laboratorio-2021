import requests
from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
from statistics import mode
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask.json import JSONEncoder
from datetime import datetime
import decimal
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

terremoto_schemas=mo.TerremotoSchema(many=True)

class JsonEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        return JSONEncoder.default(self, obj)
app.json_encoder = JsonEncoder

def stats(data):
	estadisticas={
		"mag":[0,0,0],
		"sig":[0,0,0],
		"gap":[0,0,0],
		"rms":[0,0,0]
	}

	df=pd.DataFrame(data)
	df.to_csv("text.txt")
	if not df.empty:
		for i in ['mag','gap','rms','dmin','sig']:
			
			df[i]=pd.to_numeric(df[i])
			promedio=df[i].mean()
			mediana=df[i].median()
			moda=mode(df[i].tolist())	
			estadisticas[i]=[str(promedio),str(mediana),str(moda)]

	return estadisticas


@app.route("/terremotos",methods=["GET"])
def terremotos():
	limite=request.args.get('limit')
	starttime=request.args.get('starttime')
	endtime=request.args.get('endtime')
	argumentos=request.args.to_dict()
	print(argumentos)
	
	if limite!=None:
		datos=db.session.query(mo.Terremoto).order_by(mo.Terremoto.time.desc()).limit(limite)
	else:
		datos= mo.Terremoto.query.order_by(mo.Terremoto.time.desc())
	if starttime!=None:
		datos=datos.filter(mo.Terremoto.time>=int(datetime.strptime(starttime,"%Y-%m-%d").timestamp()*1000))
	if endtime!=None:
		datos=datos.filter(mo.Terremoto.time<=int(datetime.strptime(endtime,"%Y-%m-%d").timestamp()*1000))
	datos=terremoto_schemas.dump(datos)
	estadisticas=stats(datos)
	retornar={"terremotos":datos,"estadisticas": estadisticas}

	return jsonify(retornar)






if __name__ == '__main__':
	app.run(debug=True)
