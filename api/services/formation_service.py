from ..models import formation_models
from api import db
from .teacher_service import listTeacherById


def registerFormation(formation):
    formation_db = formation_models.Formation(name=formation.name, description=formation.description)
    for i in formation.teacher:
        teacher = listTeacherById(i)
        formation_db.teacher.append(teacher)

    db.session.add(formation_db)
    db.session.commit()
    return formation_db


def listFormation():
    formation = formation_models.Formation.query.all()
    return formation


def listFormationById(id):
    formation = formation_models.Formation.query.filter_by(id=id).first()
    return formation


def updateFormation(previousFormation, formation_new):
    previousFormation.name = formation_new.name
    previousFormation.description = formation_new.description
    for i in formation_new.teacher:
        teacher = listTeacherById(i)
        previousFormation.teacher.append(teacher)
    db.session.commit()


def deleteFormation(formation):
    db.session.delete(formation)
    db.session.commit()
