from api import ma
from ..models import user_models
from marshmallow import fields


class LoginSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = user_models.User
        load_instance = True
        fields = ("id", "name", "email", "password")

    name = fields.String(required=False)
    email = fields.String(required=True)
    password = fields.String(required=True)


