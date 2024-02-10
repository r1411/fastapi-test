from sqlalchemy.orm import Session
from models import db_models, schemas
from typing import List

# Методы для создания, чтения, изменения, удаления объектов.
# По хорошему crud для каждой сущности в отдельном файле (crud_drinks, crud_...).

# Получить напиток по id
def get_drink(db: Session, drink_id: int) -> db_models.Drink:
    return db.query(db_models.Drink).filter(db_models.Drink.id == drink_id).first()

# Получить напиток по title
def get_drink_by_title(db: Session, drink_title: str) -> db_models.Drink:
    return db.query(db_models.Drink).filter(db_models.Drink.title == drink_title).first()

# Создать напиток. На вход получаем модель pydantic DrinkCreateIn
def create_drink(db: Session, drink: schemas.DrinkCreateIn) -> db_models.Drink:
    # Можем использовать model_dump(), если названия всех заполняемых полей совпадают в моделях БД и pydantic.
    # Без model_dump: 
    # db_drink = db_models.Drink(title=drink.title, volume=drink.volume, description=drink.description)
    db_drink = db_models.Drink(**drink.model_dump())
    db.add(db_drink)        # Добавить объект в сессию БД.
    db.commit()             # Сохранить изменения в базе
    db.refresh(db_drink)    # Обновить информацию об объекте из БД (чтобы подтянулся id созданного объекта)
    return db_drink

# Получить все напитки
def get_drinks(db: Session) -> List[db_models.Drink]:
    return db.query(db_models.Drink).all()

# Обновить напиток по id
def update_drink(db: Session, old_drink_id: int, new_drink: schemas.DrinkUpdateIn):
    db_drink = db.query(db_models.Drink).filter(db_models.Drink.id == old_drink_id).first()
    
    if db_drink is None:
        return None
    
    # Обновляем значения всех полей в объекте из БД
    for var, value in vars(new_drink).items():
        setattr(db_drink, var, value) if value else None
    
    db.add(db_drink)
    db.commit()
    db.refresh(db_drink)
    return db_drink

# Удалить напиток по id
def delete_drink_by_id(db: Session, drink_id: int):
    db_drink = db.query(db_models.Drink).filter(db_models.Drink.id == drink_id).first()

    if db_drink is None:
        return False
    
    db.delete(db_drink)
    db.commit()
    return True


    
