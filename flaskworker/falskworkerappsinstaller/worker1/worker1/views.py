from flask import Blueprint, request 
from project.app import make_response, jsonify, db 
from .models import UserSchema, User 
worker1_blueprint=Blueprint('worker1',__name__)




@worker1_blueprint.route("/users/", methods=(['GET']))
def all_users():
    try:
        all_users=User.query.all()
        print(all_users)
        users_schema = UserSchema(many=True)
        output=users_schema.dump(all_users)
        print(output)
        return make_response(jsonify({'users':output}, 200))
    except Exception:
        return make_response(jsonify({'Error':'unknown Error'}, 404))


@worker1_blueprint.route("/users/",methods=(['POST']))
def add_user():
    try:
        user_data=request.get_json()
        print(user_data)
        user=User(username=user_data['username'], password=user_data['password'], address=user_data['address'])
        db.session.add(user)
        db.session.commit() 
        return make_response(jsonify({'users':'user addded'}, 200))
    except Exception:
        return make_response(jsonify({'Error':'unknown Error'}, 404))

@worker1_blueprint.route("/users/<int:id>",methods=(['DELETE']))
def delete_user(id):
    try:
        user_object=User.query.filter_by(id=id)
        db.session.delete(user_object)
        db.session.commit() 
        return make_response(jsonify({'users':'user deleted'}, 200))
    except Exception:
            return make_response(jsonify({'Error':'unknown Error'}, 404))

@worker1_blueprint.route("/users/<int:id>",methods=(['PUT']))
def edit_user(id):
    try:
        user=User.query.filter_by(id=id)
        user_data=request.get_json()
        print(user[0].username)
        print(user_data['username'])
        user[0].username=user_data['username']
        user[0].address=user_data['address']
        user[0].password=user_data['password']
        db.session.commit()
        return make_response(jsonify({'users':'user updated'}, 200))
    except Exception:
            return make_response(jsonify({'Error':'unknown Error'}, 404))