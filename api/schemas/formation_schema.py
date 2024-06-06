from api import ma
from ..models import formation_models
from marshmallow import fields
from ..schemas import course_schema, teacher_schema


class FormationSchema(ma.SQLAlchemyAutoSchema):
    teacher = ma.Nested(teacher_schema.TeacherSchema, many=True, required=False, only=("id", "name"))

    class Meta:
        model = formation_models.Formation
        load_instance = True
        fields = ("id", "name", "description", "courses", "teacher", "_links")

    name = fields.String(required=True)
    description = fields.String(required=True)
    courses = fields.List(fields.Nested(course_schema.CourseSchema, only=("id", "name")))

    _links = ma.Hyperlinks(
        {"get": ma.URLFor('formationdetail', values={'id': '<id>'}),
         "put": ma.URLFor('formationdetail', values={'id': '<id>'}),
         "delete": ma.URLFor('formationdetail', values={'id': '<id>'})
         }
    )
