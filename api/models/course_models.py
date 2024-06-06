from api import db
from ..models import formation_models


class Course(db.Model):
    __tablename__ = "course"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    publicationDate = db.Column(db.Date, nullable=False)

    formation_id = db.Column(db.Integer, db.ForeignKey("formation.id"))
    formation = db.relationship(formation_models.Formation, backref=db.backref("courses", lazy="dynamic"))
 