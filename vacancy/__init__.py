from pydantic import BaseModel
from fastapi import UploadFile
class VacancyAddValidator(BaseModel):
    name: str
    description: str
    image: UploadFile
    vacancy_id: int
    level_name: str

