from flask_restful import Resource
from api import api
from ..schemas import user_schema
from flask import request, make_response, jsonify
from ..Entidades import user
from ..services import user_service
import uuid


class userList(Resource):

    def post(self):
        us = user_schema.UserSchema()
        validate = us.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            email = request.json["email"]
            password = request.json["password"]
            is_admin = request.json["is_admin"]
            api_key = str(uuid.uuid4())

            new_user = user.User(name=name, email=email, password=password, is_admin=is_admin, api_key=api_key)
            result = user_service.registerUser(new_user)
            x = us.jsonify(result)
            return make_response(x, 201)


api.add_resource(userList, '/user')

