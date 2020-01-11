import os

class Config:
    DEBUG = True
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(BASE_DIR, 'app.db')
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    CSRF_ENABLED = True
    THREADS_PER_PAGE = 2
