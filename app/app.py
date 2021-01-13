from flask import Flask
from app.extension import db
from route.destination import destination
from flask_migrate import Migrate

migrate = Migrate()


def create_app():
    """Create application factory, as explained here: http://flask.pocoo.org/docs/patterns/appfactories/.
    :param config_object: The configuration object to use.
    """
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://root:123456@127.0.0.1:3306/travel_app"
    register_extensions(app)
    register_blueprints(app)
    migrate.init_app(app, db)
    return app


def register_extensions(app):
    db.init_app(app)
    return None


def register_blueprints(app):
    """Register Flask blueprints."""
    app.register_blueprint(destination)
    return None
