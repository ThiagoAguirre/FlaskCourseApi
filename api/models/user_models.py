from api import db
from passlib.hash import pbkdf2_sha256

class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean)
    api_key = db.Column(db.String(100), nullable=True)

    def encryptPassword(self):
        self.password = pbkdf2_sha256.hash(self.password)

    def viewPassword(self, password):
        return pbkdf2_sha256.verify(password, self.password)
