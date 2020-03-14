from flask import Flask, g, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import login_user, current_user, logout_user, login_required
from flask_login import LoginManager
from todarith.commands import create_db, drop_db, populate_db, recreate_db
from todarith.database import db
from todarith.extensions import login_manager
from todarith.config import Config

from todarith.mod_auth import auth
from todarith.errors import errors
from todarith.mod_main import main
from todarith.mod_post import post
from todarith.mod_search import search

from todarith.models import User, Problem


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    #db = SQLAlchemy()
    login_manager = LoginManager()
    login_manager.init_app(app)
    db.init_app(app)

    register_blueprints(app)
    register_commands(app)
    register_extensions(app)

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
    app.register_blueprint(search, url_prefix='/search')

def register_extensions(app):
    login_manager.init_app(app)
    #db.init_app(app)
