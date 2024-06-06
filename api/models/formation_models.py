from api import db
from .teacher_models import Teacher

teacher_formation = db.Table('teacher_formation',
                             db.Column('teacher_id', db.Integer, db.ForeignKey('teacher.id'), primary_key=True,
                                       nullable=False),
                             db.Column('formation_id', db.Integer, db.ForeignKey('formation.id'), primary_key=True,
                                       nullable=False)
                             )


class Formation(db.Model):
    __tablename__ = "formation"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    teacher = db.relationship(Teacher, secondary="teacher_formation", back_populates="formation")
