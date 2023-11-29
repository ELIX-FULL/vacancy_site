from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Float
from sqlalchemy.orm import relationship

from database import Base


# Таблица пользователей
class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    reg_date = Column(DateTime)

class UserVacancy(Base):
    __tablename__ = 'vacancies'
    vacancy_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    name = Column(String)
    level_name = Column(String)
    description = Column(String)
    image = Column(String)

    user_fk = relationship(User, lazy='subquery')
