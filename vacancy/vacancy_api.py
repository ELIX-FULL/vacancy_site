from database.vacancyservice import delete_vacancy, add_vacancy, search_vacancy, edit_vacancy, search_vacancy_byname

from fastapi import APIRouter, UploadFile, File, Depends

vacancy_router = APIRouter(prefix='/vacancy', tags=['Работа с вакансиями'])



@vacancy_router.post('/add-vacancy')
async def add_new_vacancy_router(
        user_id: int, name: str,
        level_name: str, description: str,
        photo_path: UploadFile = File(...)):

    path = f'media/{photo_path.filename}'
    # Остальной код остается без изменений
    with open(path, 'wb+') as file:
        photo = await photo_path.read()
        file.write(photo)

        result = add_vacancy(user_id=user_id, name=name, level_name=level_name, description=description, image=str(f'media/{photo_path.filename}'))

    return {'status': 1, 'message': result}

@vacancy_router.delete('/delete-vacancy')
async def delete_vacancy_db(vacancy_id):
    result = delete_vacancy(vacancy_id)
    if result:
        return {"message": result}
    else:
        return {"message": 'Такой вакансии не существует'}

@vacancy_router.put('/edit-vacancy')
async def edit_vacancy_db(vacancy_id: int, choice: str, new_data: str):
    result = edit_vacancy(vacancy_id, choice, new_data)
    if result:
        return {"message": result}
    else:
        return {"message": "Такой вакансии не существует"}

@vacancy_router.put('/search-vacancy')
async def search_vacancy_db(vacancy_id):
    result = search_vacancy(vacancy_id)

    return result

@vacancy_router.put('/search-vacancy-byname')
async def search_vacancy_db(name):

    result = search_vacancy_byname(name)

    return result
