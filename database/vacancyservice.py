from database import get_db
from database.models import UserVacancy
from datetime import datetime
from fastapi import UploadFile
from typing import Optional

def add_vacancy(user_id, name, level_name, description):
    db = next(get_db())

    new_vacancy = UserVacancy(user_id=user_id, name=name, level_name=level_name,
                              description=description, vacancy_date=datetime.now())
    db.add(new_vacancy)
    db.commit()
    return 'Вакансия успешно добавлена'


def get_exact_vacancy_db(vacancy_id):
    db = next(get_db())

    exact_user = db.query(UserVacancy).filter_by(vacancy_id=vacancy_id).all()

    return exact_user
def search_vacancy_db(name, level_name, user_id):
    db = next(get_db())

    search_byname = db.query(UserVacancy).filter_by(name=name).all()
    search_bylevel = db.query(UserVacancy).filter_by(level_name=level_name).all
    search_byuserid = db.query(UserVacancy).filter_by(user_id=user_id).first()

def delete_vacancy(vacancy_id):
    db = next(get_db())

    delete_vacancy = db.query(UserVacancy).filter_by(vacancy_id).first()
    if delete_vacancy:
        db.delete(delete_vacancy)
        db.commit()
        return 'Вакансия удалена'
    else:
        return 'Вакансия не найдена'

def edit_vacancy(vacancy_id, name, description, level_name):
    db = next(get_db())

    edit_vacancy_db = db.query(UserVacancy).filter_by(vacancy_id=vacancy_id).first()

    if edit_vacancy_db:
        if name is not None:
            edit_vacancy_db.name = name
        if description is not None:
            edit_vacancy_db.description = description
        if level_name is not None:
            edit_vacancy_db.level_name = level_name

        db.commit()
        return 'Данные вакансий успешно изменены'
    else:
        return 'Вакансия не найдена'


def search_vacancy(user_id):
    db = next(get_db())

    result = db.query(UserVacancy).filter_by(user_id=user_id).first()

    if result:
        return result

    return {'status': 1, 'message': 'Error'}