from ..models import course_models
from api import db


def registerCourse(course):
    course_db = course_models.Course(name=course.name, description=course.description,
                                     publicationDate=course.publicationDate,
                                     formation=course.formation)
    db.session.add(course_db)
    db.session.commit()
    return course_db


def listCourse():
    course = course_models.Course.query.all()
    return course


def listCourseById(id):
    course = course_models.Course.query.filter_by(id=id).first()
    return course


def updateCourse(previousCourse, course_new):
    previousCourse.name = course_new.name
    previousCourse.description = course_new.description
    previousCourse.publicationDate = course_new.publicationDate
    previousCourse.formation = course_new.formation
    db.session.commit()

def deleteCourse(course):
    db.session.delete(course)
    db.session.commit()
