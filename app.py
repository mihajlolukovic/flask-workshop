from flask import Flask

from home.handlers.calculator import app
from home.handlers.home import home_bp
from home.handlers.house import house


def _initialize_blueprints(application):
    application.register_blueprint(app)
    application.register_blueprint(home_bp)
    application.register_blueprint(house)


def create_app():
    application = Flask(__name__)

    _initialize_blueprints(application)

    return application
