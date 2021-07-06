from flask import Blueprint, request 
from project import make_response, jsonify, db 
from .models import UserSchema, User 
worker1_blueprint=Blueprint('worker1',__name__)

@worker1_blueprint.route("/users/", methods=(['GET']))
def all_users():
    all_users=User.query.all()
    print(all_users)
    users_schema = UserSchema(many=True)
    output=users_schema.dump(all_users)
    print(output)
    return make_response(jsonify({'users':output}, 200))

@worker1_blueprint.route("/users/",methods=(['POST']))
def add_user():
    user_data=request.get_json()
    print(user_data)
    user=User(username=user_data['username'], password=user_data['password'], address=user_data['address'])
    db.session.add(user)
    db.session.commit() 
    return make_response(jsonify({'users':'user addded'}, 200))

@worker1_blueprint.route("/users/<int:id>",methods=(['DELETE']))
def delete_user(id):
    user_object=User.query.filter_by(id=id)
    db.session.delete(user_object)
    db.session.commit() 
    return make_response(jsonify({'users':'user deleted'}, 200))

@worker1_blueprint.route("/users/<int:id>",methods=(['PUT']))
def edit_user(id):
    user=User.query.filter_by(id=id)
    print(user[0])
    user_data=request.get_json()
    print(user_data)
    print(user_data['username'])
    for key in user_data.keys():
        user[0].key=user_data[key]
        db.session.commit()
    return make_response(jsonify({'users':'user updated'}, 200))
