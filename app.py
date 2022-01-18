from flask import Flask


def _initialize_blueprints(application):
    from home.handlers.calculator import app
    application.register_blueprint(app)


def create_app():
    application = Flask(__name__)

    _initialize_blueprints(application)

    return application
