from db import db_engine

# Здесь храним ссылки на зависимости

# Зависимость БД. Создает сессию, после окончания использования закрывает ее.
def get_db():
    db = db_engine.SessionLocal()
    try:
        yield db
    finally:
        db.close()