from pydantic import BaseModel

# Здесть храним модели pydantic
# По хорошему модели для каждой сущнсти в отдельном файле

# Базовая модель, содержит поля, которые будут во всех моделях-потомках
class DrinkBase(BaseModel):
    title: str
    volume: int
    description: str | None = None # Тип - str | None (str или None), дефолтное значение - None

    # Необходимо для работы ORM (а именно для заполнения полей-связей)
    class Config:
        from_attributes = True

# Модель данных, принимаемых от клиента при создании объекта. В данном случае это три поля - title, volume, description - они уже есть в DrinkBase.
class DrinkCreateIn(DrinkBase):
    pass

# Модель данных, отдаваемых клиенту после создания объекта. Здесь все что в DrinkBase + id созданного объекта
class DrinkCreateOut(DrinkBase):
    id: int

# Модель с данными, возвращаемыми клиенту при чтении объекта.
class Drink(DrinkBase):
    id: int

# Модель данных, принимаемых от клиента при изменении объекта.
class DrinkUpdateIn(DrinkBase):
    pass

# Модель данных, возвращаемых клиенту после изменения объекта
class DrinkUpdateOut(DrinkBase):
    id: int