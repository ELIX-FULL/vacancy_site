from fastapi import FastAPI
import uvicorn
from user.user_api import user_router
from vacancy.vacancy_api import vacancy_router


from database import Base, engine
Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url='/')

app.include_router(user_router)
app.include_router(vacancy_router)
# app.include_router()



#
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8482)