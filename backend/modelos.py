from flask_sqlalchemy import SQLAlchemy 
from marshmallow import Schema, fields, ValidationError, pre_load
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from sqlalchemy.orm import backref

from sqlalchemy.schema import CreateColumn
from sqlalchemy.ext.compiler import compiles

db=SQLAlchemy()

class Terremoto(db.Model):
	__tablename__ = 'terremoto'
	id = db.Column(db.String, primary_key=True)
	mag= db.Column(db.Numeric,nullable=True)
	place= db.Column(db.Text,nullable=True)
	time= db.Column(db.BigInteger,nullable=True)
	updated= db.Column(db.BigInteger,nullable=True)
	tz= db.Column(db.Integer, nullable=True)
	url= db.Column(db.Text,nullable=True)
	detail= db.Column(db.Text,nullable=True)
	felt=db.Column(db.Integer, nullable=True)
	cdi= db.Column(db.Numeric,nullable=True)
	mmi= db.Column(db.Numeric,nullable=True)
	alert= db.Column(db.Text,nullable=True)
	status= db.Column(db.Text,nullable=True)
	tsunami= db.Column(db.Integer, nullable=True)
	sig=db.Column(db.Integer, nullable=True)
	net= db.Column(db.Text,nullable=True)
	code= db.Column(db.Text,nullable=True)
	ids= db.Column(db.Text,nullable=True)
	sources= db.Column(db.Text,nullable=True)
	types= db.Column(db.Text,nullable=True)
	nst= db.Column(db.Integer, nullable=True)
	dmin= db.Column(db.Numeric,nullable=True)
	rms= db.Column(db.Numeric,nullable=True)
	gap= db.Column(db.Numeric,nullable=True)
	mag_type= db.Column(db.Text,nullable=True)
	tipe= db.Column(db.Text,nullable=True)


	
	def __init__(self,d):
		self.id=d["id"]
		self.mag=d["mag"]
		self.place=d["place"]
		self.time=d["time"]
		self.updated=d["updated"]
		self.tz=d["tz"]
		self.url=d["url"]
		self.detail=d["detail"]
		self.felt=d["felt"]
		self.cdi=d["cdi"]
		self.mmi=d["mmi"]
		self.alert=d["alert"]
		self.status=d["status"]
		self.tsunami=d["tsunami"]
		self.sig=d["sig"]
		self.net=d["net"]
		self.code=d["code"]
		self.ids=d["ids"]
		self.sources=d["sources"]
		self.types=d["types"]
		self.nst=d["nst"]
		self.dmin=d["dmin"]
		self.rms=d["rms"]
		self.gap=d["gap"]
		self.mag_type=d["magType"]
		self.tipe=d["type"]
class TerremotoSchema(SQLAlchemyAutoSchema):
	class Meta:
		fields = ('mag','place','time','updated','tz','url','detail','felt','cdi','mmi','alert','status','tsunami','sig',
		'net','code','ids','sources','types','nst','dmin','rms','gap','mag_type','tipe')

def objeto_db():
	global db
	return db