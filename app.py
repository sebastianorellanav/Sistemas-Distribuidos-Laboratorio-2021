from operator import mod
from typing import Text
import requests
from flask import Flask, jsonify, request,make_response
import json


app= Flask(__name__)

"""
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/cai"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
db.init_app(app)

ma = Marshmallow(app)
migrate= Migrate(app,db)
"""


@app.route("/terremotos",methods=["GET"])
def get_info():
	parm=request.args.to_dict()
	request_data= requests.get("https://earthquake.usgs.gov/fdsnws/event/1/query",params=parm)
	request_data=request_data.json()
	request_data=request_data["features"]
	respuesta=[]

	return jsonify(request_data)



if __name__ == '__main__':
	app.run(debug=True)