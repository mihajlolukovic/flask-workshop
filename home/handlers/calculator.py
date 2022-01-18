from flask import Blueprint, jsonify

from home.services.calculator_service import CalculatorService

app = Blueprint('fl', __name__)

calculator_service = CalculatorService()


@app.route('/sum/num/<int:first_number>/<int:second_number>', methods=['GET'])
def summation(first_number, second_number):
    summa = calculator_service.summation(first_number, second_number)
    return jsonify(sum=summa)


@app.route('/sub/num/<int:first_number>/<int:second_number>', methods=['GET'])
def subtraction(first_number, second_number):
    subtract = calculator_service.subtraction(first_number, second_number)
    return jsonify(sum=subtract)


@app.route('/mul/num/<int:first_number>/<int:second_number>', methods=['GET'])
def multiplication(first_number, second_number):
    multiply = calculator_service.multiplication(first_number, second_number)
    return jsonify(sum=multiply)


@app.route('/div/num/<int:first_number>/<int:second_number>', methods=['GET'])
def divide(first_number, second_number):
    div = calculator_service.divide(first_number, second_number)
    return jsonify(sum=div)



