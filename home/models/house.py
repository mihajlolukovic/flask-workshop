from sqlalchemy import (Column, Integer, String)


class House:
    id = Column(Integer, primary_key=True)
    street = Column(String(100))
    number = Column(Integer)

    def __init__(self, street, number):
        self.street = street
        self.number = number
