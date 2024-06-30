from extensions import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin


class BaseModel:

    def create(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def save():
        db.session.commit()

class BMI(db.Model, BaseModel):

    __tablename__ = "bmis"

    id = db.Column(db.Integer(), primary_key=True)
    weight = db.Column(db.Integer(), nullable=False)
    height = db.Column(db.Float(), nullable=False)



class User(db.Model, BaseModel, UserMixin):

    __tablename__ = "users"

    id = db.Column(db.Integer(), primary_key=True)
    firstname = db.Column(db.String())
    lastname = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    role = db.Column(db.String())


    def __init__(self, firstname, lastname, email, password, role = "Guest"):
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = generate_password_hash(password)
        self.role = role

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Calories(db.Model, BaseModel):

    __tablename__ = "calories"

    id = db.Column(db.Integer(), primary_key=True)
    age = db.Column(db.Integer())
    weight = db.Column(db.Integer())
    height = db.Column(db.Integer())

    def __init__(self, weight, height, age, ):
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self):
        result = 10 * self.weight + 6.5 * self.height + 5 * self.age + 5
        return round(result)

class Message(db.Model, BaseModel):
    __tablename__ = "messages"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String)
    email = db.Column(db.String)
    message = db.Column(db.String)








