from flask_restful import Resource
from api import api
from ..schemas import formation_schema
from flask import request, make_response, jsonify
from ..Entidades import formation
from ..services import formation_service
from ..paginate import paginate
from ..models.formation_models import Formation
from flask_jwt_extended import jwt_required


class formationList(Resource):
    @jwt_required()
    def get(self):
        cs = formation_schema.FormationSchema(many=True)
        return paginate(Formation, cs)
    @jwt_required()
    def post(self):
        cs = formation_schema.FormationSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            teacher = request.json["teacher"]
            new_formation = formation.Formation(name=name, description=description, teacher=teacher)
            result = formation_service.registerFormation(new_formation)
            x = cs.jsonify(result)
            return make_response(x, 201)


class formationDetail(Resource):
    @jwt_required()
    def get(self, id):
        formation = formation_service.listFormationById(id)
        if formation is None:
            return make_response(jsonify("formation not found!"), 404)
        cs = formation_schema.FormationSchema()
        return make_response(cs.jsonify(formation), 200)
    @jwt_required()
    def put(self, id, cs):
        formation_db = formation_service.listFormationById(id)
        if formation_db is None:
            return make_response(jsonify("Formation not found!"), 404)
        cs = formation_schema.FormationSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            teacher = request.json["teacher"]
            new_formation = formation.Formation(name=name, description=description, teacher=teacher)
            formation_service.updateFormation(formation_db, new_formation)
            formation_update = formation_service.listFormationById(id)
            return make_response(cs.jsonify(formation_update), 200)

    @jwt_required()
    def delete(self, id):
        formation_db = formation_service.listFormationById(id)
        if formation_db is None:
            return make_response(jsonify("Formation not found"), 404)
        formation_service.deleteFormation(formation_db)
        return make_response("Formation is delete success", 204)


api.add_resource(formationList, '/formation')
api.add_resource(formationDetail, '/formation/<int:id>')
