import os
from flaskext.mysql import MySQL

class Config:
    DEBUG = True
    """
    #BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    #SQLALCHEMY_DATABASE_URI = 'sqlite://' + os.path.join(BASE_DIR, 'app.db')
    #SQLALCHEMY_DATABASE_URI = ''
    #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:8a9cbor4@localhost/todarith'
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db'
    MYSQL_USER = 'epiz_25094715'
    MYSQL_PASSWORD = 'QT7BmdgeAnf0Op'
    MYSQL_DB = 'todarith'
    MYSQL_HOST = 'localhost'

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://epiz_25094715:QT7BmdgeAnf0Op@sql207.epizy.com:3307/epiz_25094715_todarith'
    """

    POSTGRES = {
        'user': 'lukew3',
        'pw': '8a9cbor4',
        'db': 'todarith',
        'host': 'localhost',
        'port': '5432',
    }
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    #CSRF_SESSION_KEY = "secret"
    SECRET_KEY = "secret"
    CSRF_ENABLED = True
    #THREADS_PER_PAGE = 2
