from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#from flask_login import login_user, current_user, logout_user, login_required
from flask_login import LoginManager
from todarith.config import Config


db = SQLAlchemy()
login_manager = LoginManager()

#@app.errorhandler(404)
#def not_found(error):
#    return render_template('404.html'), 404


# Build the database:
#This will create the database file using SQLAlchemy
#db.create_all()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from todarith.mod_auth.controller import auth
    from todarith.errors.handlers import errors
    from todarith.mod_main.controller import main
    from todarith.mod_post.controller import post
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(errors)
    app.register_blueprint(main)
    app.register_blueprint(post, url_prefix='/post')

    return app
