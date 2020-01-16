import os

class Config:
    DEBUG = True
    #BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_DATABASE_URI = 'mysql://sql9318896:whlSMpD33C@sql9.freemysqlhosting.net/mydatabase'
    MYSQL_DATABSE_HOST = 'localhost'
    MYSQL_DATABASE_USER = 'root'
    MYSQL_DATABASE_PASSWORD = '8a9cbor4'
    MYSQL_DATABASE_DB = 'todarith'
    DATABASE_CONNECT_OPTIONS = {}
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    CSRF_ENABLED = True
    THREADS_PER_PAGE = 2
