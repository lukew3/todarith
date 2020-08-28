import os
import json

with open('/etc/config.json') as config_file:
	config = json.load(config_file)

class Config:
    DEBUG = True

    """Default configuration options."""
    #SITE_NAME = os.environ.get('APP_NAME', 'Todarith')

    SECRET_KEY = config.get('SECRET_KEY', 'secrets')
    #SERVER_NAME = os.environ.get('SERVER_NAME', 'app.docker:5000')

    #MAIL_SERVER = os.environ.get('MAIL_SERVER', 'mail')
    #MAIL_PORT = os.environ.get('MAIL_PORT', 1025)

    #REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    #REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    #RQ_REDIS_URL = 'redis://{}:{}'.format(REDIS_HOST, REDIS_PORT)

    #CACHE_HOST = os.environ.get('MEMCACHED_HOST', 'memcached')
    #CACHE_PORT = os.environ.get('MEMCACHED_PORT', 11211)

    POSTGRES_HOST = config.get('POSTGRES_HOST', 'postgres')
    POSTGRES_PORT = config.get('POSTGRES_PORT', 5432)
    POSTGRES_USER = config.get('POSTGRES_USER', 'postgres')
    POSTGRES_PASS = config.get('POSTGRES_PASS', 'postgres')
    POSTGRES_DB = config.get('POSTGRES_DB', 'postgres')

    SQLALCHEMY_DATABASE_URI = 'postgresql://%s:%s@%s:%s/%s' % (
        POSTGRES_USER,
        POSTGRES_PASS,
        POSTGRES_HOST,
        POSTGRES_PORT,
        POSTGRES_DB
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SUPPORTED_LOCALES = ['en']

"""
class dev_config(base_config):
    #Development configuration options.
    ASSETS_DEBUG = True
    WTF_CSRF_ENABLED = False

class test_config(base_config):
    #Testing configuration options.
    TESTING = True
    WTF_CSRF_ENABLED = False
"""
