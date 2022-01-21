from flask import jsonify

from home.db.connection import DBConnection
from home.models.house import House


class HouseService(DBConnection):
    def add_house(self, street, number):
        house = House(street=street, number=number)
        session = self.db_connection()
        session.add(house)
        session.commit()
        return jsonify(street=street, number=number), 201
