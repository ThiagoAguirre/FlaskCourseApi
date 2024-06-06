from api import ma
from ..models import course_models
from marshmallow import fields


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = course_models.Course
        load_instance = True
        fields = ("id", "name", "description", "publicationDate", "formation", "_links")

    name = fields.String(required=True)
    description = fields.String(required=True)
    publicationDate = fields.Date(required=True)
    formation = fields.String(required=True)

    _links = ma.Hyperlinks(
        {"get": ma.URLFor('cursodetail', values={'id': '<id>'}),
         "put": ma.URLFor('cursodetail', values={'id': '<id>'}),
         "delete": ma.URLFor('cursodetail', values={'id': '<id>'})
         }
    )
