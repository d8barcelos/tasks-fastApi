from fastapi import FastAPI
from database import engine, Base
from routes import users_router, tasks_router

# Cria tabelas no banco de dados
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclui as rotas
app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(tasks_router, prefix="/tasks", tags=["tasks"])
