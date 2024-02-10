from typing import Any, List, Union
from fastapi import Depends, APIRouter, Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session
from models import schemas
from services import drinks_service
from api.dependencies import get_db

router = APIRouter()

# Получение всех напитков
@router.get("", response_model=List[schemas.Drink])
def get_drinks(db: Session = Depends(get_db)):
    return drinks_service.get_all_drinks(db)

# Получение напитка по id
@router.get("/{drink_id}", response_model=schemas.Drink)
def get_drink_by_id(drink_id: int, db: Session = Depends(get_db)):
    return drinks_service.get_drink_by_id(db, drink_id)

# Создание напитка
@router.post("", response_model=schemas.DrinkCreateOut)
def create_drink(drink: schemas.DrinkCreateIn, db: Session = Depends(get_db)):
    return drinks_service.create_drink(db, drink)

# Изменение напитка по id
@router.put("/{drink_id}", response_model=schemas.DrinkUpdateOut)
def update_drink_by_id(drink_id: int, new_drink: schemas.DrinkUpdateIn, db: Session = Depends(get_db)):
    return drinks_service.update_drink(db, drink_id, new_drink)

# Удаление напитка по id
@router.delete("/{drink_id}")
def delete_drink_by_id(drink_id: int, db: Session = Depends(get_db)):
    drinks_service.delete_drink(db, drink_id)
    return Response(status_code=HTTP_204_NO_CONTENT)