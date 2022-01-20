from flask import Flask

from home.handlers.calculator import app
from home.handlers.home import home_bp


def _initialize_blueprints(application):
    application.register_blueprint(app)
    application.register_blueprint(home_bp)


def create_app():
    application = Flask(__name__)

    _initialize_blueprints(application)

    return application
