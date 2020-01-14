import os

class Config:
    DEBUG = True
    #BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_DATABASE_URI = ''
    MYSQL_HOST = 'sql3.freemysqlhosting.net'
    MYSQL_USER = 'sql9318896'
    MYSQL_PASSWORD = 'whlSMpD33C'
    MYSQL_DB = 'sql9318896'
    MYSQL_CHARSET = 'utf-8'
    MYSQL_CURSORCLASS = 'DictCursor'
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    CSRF_ENABLED = True
    THREADS_PER_PAGE = 2
