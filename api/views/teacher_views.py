from flask_restful import Resource
from api import api
from ..schemas import teacher_schema
from flask import request, make_response, jsonify
from ..Entidades import teacher
from ..services import teacher_service
from ..paginate import paginate
from ..models.teacher_models import Teacher


class teacherList(Resource):
    def get(self):
        ts = teacher_schema.TeacherSchema(many=True)
        return paginate(Teacher, ts)

    def post(self):
        ts = teacher_schema.TeacherSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            age = request.json["age"]

            new_teacher = teacher.Teacher(name=name, age=age)
            result = teacher_service.registerTeacher(new_teacher)
            x = ts.jsonify(result)
            return make_response(x, 201)


class teacherDetail(Resource):
    def get(self, id):
        teacher = teacher_service.listTeacherById(id)
        if teacher is None:
            return make_response(jsonify("teacher not found!"), 404)
        ts = teacher_schema.TeacherSchema()
        return make_response(ts.jsonify(teacher), 200)

    def put(self, id):
        teacher_db = teacher_service.listTeacherById(id)
        if teacher_db is None:
            return make_response(jsonify("teacher not found!"), 404)
        ts = teacher_schema.TeacherSchema()
        validate = ts.validate(request.json)
        if validate:
            return make_response(jsonify(validate), 400)
        else:
            name = request.json["name"]
            age = request.json["age"]
            new_teacher = teacher.Teacher(name=name, age=age)

            teacher_service.updateTeacher(teacher_db, new_teacher)
            teacher_update = teacher_service.listTeacherById(id)
            return make_response(ts.jsonify(teacher_update), 200)

    def delete(self, id):
        teacher_db = teacher_service.listTeacherById(id)
        if teacher_db is None:
            return make_response(jsonify("Teacher not found"), 404)
        teacher_service.deleteTeacher(teacher_db)
        return make_response("Teacher is delete success", 204)


api.add_resource(teacherList, '/teacher')
api.add_resource(teacherDetail, '/teacher/<int:id>')
