from fastapi import FastAPI
from typing import Union
from config.settings import settings
from db import db_engine
from models import db_models
from api.api import api_router

# Создать таблицы в БД, если их нет. 
# В дальнейшем возможно перейдем на миграции через Alembic, чтобы не ломалась база при изменении полей сущностей.
db_models.Base.metadata.create_all(bind=db_engine.engine)

app = FastAPI()

app.include_router(api_router, prefix=settings.API_BASE_STR)