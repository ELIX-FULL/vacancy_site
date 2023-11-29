from datetime import datetime
from database.vacancyservice import delete_vacancy, add_vacancy, search_vacancy, edit_vacancy
from fastapi import APIRouter
from vacancy import VacancyAddValidator
vacancy_router = APIRouter(prefix='/vacancy', tags=['Работа с вакансиями'])

@vacancy_router.post('/add-vacancy')
async def add_new_vacancy_router(data: VacancyAddValidator):
    new_vacancy_data = data.model_dump()
    result = add_vacancy(vacancy_date=datetime.now(), **new_vacancy_data)
    return {'message': result}

@vacancy_router.delete('/delete-vacancy')
async def delete_vacancy_db(vacancy_id):
    result = delete_vacancy(vacancy_id)
    if result:
        return {"message": result}
    else:
        return {"message": 'Такой вакансии не существует'}

@vacancy_router.put('/edit-vacancy')
async def edit_vacancy_db(vacancy_id):
    result = edit_vacancy(vacancy_id)
    if result:
        return {"message": result}
    else:
        return {"message": "Такой вакансии не существует"}

@vacancy_router.put('/search-vacancy')
async def search_vacancy_db(vacancy_id):
    result = search_vacancy(vacancy_id)

    return result
