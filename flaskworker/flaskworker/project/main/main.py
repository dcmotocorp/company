import os 
from flask import Flask, jsonify, make_response  
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from jinja2.loaders import PrefixLoader 
from flask_marshmallow import Marshmallow

app= Flask(__name__)
ma = Marshmallow(app)
basefile= os.path.abspath(os.path.dirname(__file__))
app.config['SECREAT_KEY']='mypassword'
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'+ os.path.join(basefile,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db=SQLAlchemy(app)
import worker1.models

Migrate(app,db)
from project.worker2.views import worker2_blueprint
from worker1.views import worker1_blueprint
app.register_blueprint(worker1_blueprint, url_prefix='/worker1')
app.register_blueprint(worker2_blueprint, url_prefix='/worker2')