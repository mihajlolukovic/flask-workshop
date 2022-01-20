from flask import Blueprint

from home.services.home_service import HomeService

home_bp = Blueprint('home_bp', __name__)


class Home:
    home_service = HomeService()

    # Landing page
    home_bp.add_url_rule('/', view_func=home_service.index)

