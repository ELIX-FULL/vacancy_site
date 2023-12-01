from database import get_db
from database.models import UserVacancy
from datetime import datetime
from fastapi import UploadFile


def add_vacancy(user_id, name, level_name, description, image):
    db = next(get_db())

    new_vacancy = UserVacancy(user_id=user_id, name=name, level_name=level_name,
                              description=description, image=image)

    db.add(new_vacancy)
    db.commit()

    return f'Вакансия успешно добавлена id - {new_vacancy.vacancy_id}'


def delete_vacancy(vacancy_id):
    db = next(get_db())

    delete_vacancy = db.query(UserVacancy).filter_by(vacancy_id=vacancy_id).first()
    if delete_vacancy:
        db.delete(delete_vacancy)
        db.commit()
        return 'Вакансия удалена'
    else:
        return 'Вакансия не найдена'


def edit_vacancy(vacancy_id, choice, new_data):
    db = next(get_db())

    edit_vacancy_db = db.query(UserVacancy).filter_by(vacancy_id=vacancy_id).first()

    if edit_vacancy_db:
        if choice == 'name':
            edit_vacancy_db.name = new_data
        elif choice == 'description':
            edit_vacancy_db.description = new_data
        elif choice == 'level_name':
            edit_vacancy_db.level_name = new_data

        db.commit()
        return 'Данные вакансий успешно изменены'

    else:
        return 'Вакансия не найдена'


def search_vacancy(vacancy_id):
    db = next(get_db())

    result = db.query(UserVacancy).filter_by(vacancy_id=vacancy_id).first()

    if result:
        return result

    return {'status': 1, 'message': 'Error'}


def search_vacancy_byname(name):
    db = next(get_db())

    result = db.query(UserVacancy).filter_by(name=name).first()

    if result:
        return result

    return {'status': 1, 'message': 'Error'}
