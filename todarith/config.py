import os

class Config:
    DEBUG = True
    #BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_DATABASE_URI = ''
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8a9cbor4@localhost/todarith'
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
    SQLALCHEMY_DATABASE_URI = 'mysql://epiz_25094715:QT7BmdgeAnf0Op@sql207.epizy.com/epiz_25094715_todarith'
    CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    CSRF_ENABLED = True
    THREADS_PER_PAGE = 2
