from ..models import user_models
from api import db


def registerUser(user):
    user_db = user_models.User(name=user.name, email=user.email, password=user.password, is_admin=user.is_admin, api_key=user.api_key)
    user_db.encryptPassword()
    db.session.add(user_db)
    db.session.commit()
    return user_db


def listUserEmail(email):
    return user_models.User.query.filter_by(email=email).first()

def listUserById(id):
    return user_models.User.query.filter_by(id=id).first()

def listUserApiKey(api_key):
    return user_models.User.query.filter_by(api_key=api_key).first()


