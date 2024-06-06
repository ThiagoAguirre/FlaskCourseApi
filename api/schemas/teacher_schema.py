from api import ma
from ..models import teacher_models
from marshmallow import fields


class TeacherSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = teacher_models.Teacher
        load_instance = True
        fields = ("id", "name", "age", "_links")

    name = fields.String(required=True)
    age = fields.Integer(required=True)

    _links = ma.Hyperlinks(
        {"get": ma.URLFor('teacherdetail', values={'id': '<id>'}),
         "put": ma.URLFor('teacherdetail', values={'id': '<id>'}),
         "delete": ma.URLFor('teacherdetail', values={'id': '<id>'})
         }
    )
