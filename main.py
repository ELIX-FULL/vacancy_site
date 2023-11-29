from fastapi import FastAPI

from user.user_api import user_router
from vacancy.vacancy_api import vacancy_router


from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(vacancy_router)
# app.include_router()




