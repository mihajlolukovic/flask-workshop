from flask import jsonify


class CalculatorService:

    @staticmethod
    def summation(first_number, second_number):
        result = first_number + second_number
        return jsonify(total=result)

    @staticmethod
    def subtraction(first_number, second_number):
        result = first_number - second_number
        return jsonify(total=result)

    @staticmethod
    def multiplication(first_number, second_number):
        result = first_number * second_number
        return jsonify(total=result)

    @staticmethod
    def divide(first_number, second_number):
        result = first_number / second_number
        return jsonify(total=result)
