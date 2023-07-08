from sqlalchemy import inspect
from app.db import db
from flask_login import UserMixin

class BaseMixin(db.Model):
    __abstract__ = True

    def __int__(self, **kwargs):
        self.__dict__.update(kwargs)

    def to_dict(self):
        return {c.key: getattr(self, c.key)
                for c in inspect(self).mapper.column_attrs}


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

class Employee(BaseMixin):
    __tablename__ = 'employees'

    id = db.Column(db.Integer, primary_key=True)
    surname = db.Column(db.String(30), nullable=False)
    second_name = db.Column(db.String(30), nullable=False)
    firstname = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)

class Position(BaseMixin):
    __tablename__ = 'positions'

    id = db.Column(db.Integer, primary_key=True)
    name_position = db.Column(db.String(50), nullable=False)

class Division(BaseMixin):
    __tablename__ = 'divisions'

    id = db.Column(db.Integer, primary_key=True)
    name_division = db.Column(db.String, nullable=False)
class Job(BaseMixin):
    __tablename__ = 'job'

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=True)
    position_id = db.Column(db.Integer, db.ForeignKey('positions.id'), nullable=True)
    division_id = db.Column(db.Integer, db.ForeignKey('divisions.id'), nullable=True)
    date_of_employment = db.Column(db.Date, nullable=True)
    date_of_dismissal = db.Column(db.Date, nullable=True)