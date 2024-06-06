from flask_restful import Resource
from api import api
from ..schemas import course_schema
from flask import request, make_response, jsonify
from ..Entidades import course
from ..services import course_service, formation_service
from ..paginate import paginate
from ..models.course_models import Course
from flask_jwt_extended import jwt_required, get_jwt
from ..decorator import admin_required, api_key_required


class cursoList(Resource):
    @admin_required
    def get(self):
        cs = course_schema.CourseSchema(many=True)
        return paginate(Course, cs)

    @admin_required
    def post(self):

        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            publicationDate = request.json["publicationDate"]
            formation = request.json["formation"]
            formation_course = formation_service.listFormationById(formation)
            if formation_course is None:
                return make_response(jsonify("formation not found"), 404)
            new_course = course.Curso(name=name, description=description,
                                      publicationDate=publicationDate, formation=formation_course)
            result = course_service.registerCourse(new_course)
            x = cs.jsonify(result)
            return make_response(x, 201)


class cursoDetail(Resource):
    @admin_required
    def get(self, id):
        course = course_service.listCourseById(id)
        if course is None:
            return make_response(jsonify("course not found!"), 404)
        cs = course_schema.CourseSchema()
        return make_response(cs.jsonify(course), 200)

    @admin_required
    def put(self, id):
        course_db = course_service.listCourseById(id)
        if course_db is None:
            return make_response(jsonify("course not found!"), 404)
        cs = course_schema.CourseSchema()
        validate = cs.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            description = request.json["description"]
            publicationDate = request.json["publicationDate"]
            formation = request.json["formation"]
            formation_course = formation_service.listFormationById(formation)
            if formation_course is None:
                return make_response(jsonify("formation not found"), 404)
            new_course = course.Curso(name=name, description=description, publicationDate=publicationDate,
                                      formation=formation_course)
            course_service.updateCourse(course_db, new_course)
            course_update = course_service.listCourseById(id)
            return make_response(cs.jsonify(course_update), 200)

    @admin_required
    def delete(self, id):
        course_db = course_service.listCourseById(id)
        if course_db is None:
            return make_response(jsonify("course not found"), 404)
        course_service.deleteCourse(course_db)
        return make_response("Course is delete success", 204)


api.add_resource(cursoList, '/course')
api.add_resource(cursoDetail, '/course/<int:id>')
