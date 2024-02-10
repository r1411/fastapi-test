class Settings():
    API_BASE_STR: str = "/api/v1"
    DB_URI = 'sqlite:///./sql_app.db'
    DB_CONNECT_ARGS = {"check_same_thread": False}
    SUPERUSER_USERNAME = 'admin'
    SUPERUSER_EMAIL = 'admin@example.com'
    SUPERUSER_PASSWORD = '123456'
    SUPERUSER_DISPLAYNAME = 'Administrator'

settings = Settings()