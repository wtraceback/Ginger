from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer
from datetime import datetime

db = SQLAlchemy()

class Base(db.Model):
    __abstract__ = True

    create_time = Column(Integer)

    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    @property
    def create_datetime(self):
        if self.create_datetime:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None
