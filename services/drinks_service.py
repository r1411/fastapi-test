from sqlalchemy.orm import Session
from typing import List
from models import schemas
from crud import crud
from fastapi import HTTPException

# Здесь живет вся бизнес логика про напитки. Отсюда обращаемся к crud, сюда обращаемся из endpoint'ов.
# В простых случаях - просто обращаемся к crud.

def get_all_drinks(db: Session):
    return crud.get_drinks(db)

def get_drink_by_id(db: Session, drink_id: int):
    return crud.get_drink(db, drink_id)

def create_drink(db: Session, drink: schemas.DrinkCreateIn):
    existing_drink = crud.get_drink_by_title(db, drink.title)
    if existing_drink:
        raise HTTPException(status_code=400, detail="Drink with this title already exists")
    
    return crud.create_drink(db, drink)

def update_drink(db: Session, old_drink_id: int, new_drink: schemas.DrinkUpdateIn):
    existing_drink = crud.get_drink(db, old_drink_id)
    if not existing_drink:
        raise HTTPException(status_code=400, detail="This drink does not exist")
    
    return crud.update_drink(db, old_drink_id, new_drink)

def delete_drink(db: Session, drink_id: int):
    existing_drink = crud.get_drink(db, drink_id)
    if not existing_drink:
        raise HTTPException(status_code=400, detail="This drink does not exist")
    
    return crud.delete_drink_by_id(db, drink_id)