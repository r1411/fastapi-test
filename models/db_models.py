from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from db.db_engine import Base

# Здесь храним модели объектов, хранящихся в БД
# По хорошему каждая сущнсть в отдельном файле

class Drink(Base):
    __tablename__ = "drinks"

    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True, nullable=False)
    volume = Column(Integer, nullable=False)
    description = Column(String, nullable=True)