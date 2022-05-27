import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = sq.Column(sq.Integer, primary_key=True)
    username = sq.Column(sq.Text, unique=True)
    email = sq.Column(sq.Text, unique=True)
    password_hash = sq.Column(sq.Text)


class Operation(Base):
    __tablename__ = 'operations'

    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.id'))
    type = sq.Column(sq.String)
    date = sq.Column(sq.Date)
    description = sq.Column(sq.String, nullable=True)
    amount = sq.Column(sq.Numeric(10, 2))
