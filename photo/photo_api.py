from fastapi import APIRouter, UploadFile

photo_router = APIRouter(prefix='/photo', tags=['Загрузка изображений вакансий'])


# Добавления фото(для вакансий)
@photo_router.post('/add-vacancy-photo')
async def add_user_vacancy_photo(photo_file: UploadFile):
    # Сохранить локально фото
    with open(f'media/{photo_file.filename}', 'wb') as file:
        user_photo = await photo_file.read()

        file.write(user_photo)

    return {'message': 'Успешно'}


# Изменения фото(для Вакансий)
@photo_router.put('/edit-vacancy-photo')
async def edit_user_vacancy_photo(new_photo_file: UploadFile, user_id: int):
    # Сохранить локально фото
    with open(f'media/{new_photo_file.filename}', 'wb') as file:
        user_photo = await new_photo_file.read()

        file.write(user_photo)

    return {'message': 'Успешно'}


# Удаления фото(ля вакансий)
# @photo_router.delete('/delete-vacancy-photo')
# async def delete_user_vacancy_photo(vacancy_id: int):
#     delete_vacancy_photo = de