from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, logout_user, login_required
from flask_login import LoginManager
from todarith.commands import create_db, drop_db, populate_db, recreate_db
from todarith.database import db
from todarith import config

from todarith.mod_auth import auth
from todarith.errors import errors
from todarith.mod_main import main
from todarith.mod_post import post

#from todarith.config import base_config

#mysql = MySQL()

def create_app(config=config.base_config):
    app = Flask(__name__)
    app.config.from_object(config)

    #db = SQLAlchemy()
    login_manager = LoginManager()

    register_blueprints(app)
    register_commands(app)

    db.init_app(app)
    login_manager.init_app(app)

    from todarith.mod_auth.controller import auth
    from todarith.errors.handlers import errors
    from todarith.mod_main.controller import main
    from todarith.mod_post.controller import post

    return app

def register_commands(app):
    """Register custom commands for the Flask CLI."""
    for command in [create_db, drop_db, populate_db, recreate_db]:
        app.cli.command()(command)

def register_blueprints(app):
    """Register blueprints with the Flask application."""
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(post, url_prefix='/post')
