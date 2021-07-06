from flask import Blueprint
from flask.wrappers import Response 
import json
from urllib.request import urlopen 

#define blueprint 
worker2_blueprint=Blueprint('worker2',__name__)

#fetch data from external api 
@worker2_blueprint.route('/user/<int:id>')
def get(id):
        data = json.load(urlopen('https://jsonplaceholder.typicode.com/posts/' + str(id)))
        print(type(data))
        data=json.dumps(data)
        return Response(data)