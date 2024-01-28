from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.models.base import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    _password = Column('password', String(200))
    nickname = Column(String(24), unique=True)
    auth = Column(SmallInteger, default=1)

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(account, secret, nickname):
        try:
            print("准备写数据库")
            from .base import db
            user = User()
            user.email = account
            user.password = secret
            user.nickname = nickname
            db.session.add(user)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print("写数据库失败")
            raise e
