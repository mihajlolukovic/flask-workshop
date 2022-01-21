from flask import Blueprint

from home.services.house_service import HouseService

house = Blueprint('house', __name__)


class House:
    house_service = HouseService()

    # Add house
    house.add_url_rule(
        '/add_house/<street>/<int:number>',
        view_func=house_service.add_house,
        methods=['POST']
    )
