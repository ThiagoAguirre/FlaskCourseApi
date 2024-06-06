from ..models import teacher_models
from api import db


def registerTeacher(teacher):
    teacher_db = teacher_models.Teacher(name=teacher.name, age=teacher.age)
    db.session.add(teacher_db)
    db.session.commit()
    return teacher_db


def listTeacher():
    teacher = teacher_models.Teacher.query.all()
    return teacher


def listTeacherById(id):
    teacher = teacher_models.Teacher.query.filter_by(id=id).first()
    return teacher


def updateTeacher(previousTeacher, teacher_new):
    previousTeacher.name = teacher_new.name
    previousTeacher.age = teacher_new.age
    db.session.commit()


def deleteTeacher(teacher):
    db.session.delete(teacher)
    db.session.commit()
