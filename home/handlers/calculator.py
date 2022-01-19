from flask import Blueprint

from home.services.calculator_service import CalculatorService

app = Blueprint('fl', __name__)


class Calculator:

    calculation = CalculatorService()

    # Sum two numbers
    app.add_url_rule(
        '/sum/num/<int:first_number>/<int:second_number>',
        view_func=calculation.summation
    )

    # Sub two numbers
    app.add_url_rule(
        '/sub/num/<int:first_number>/<int:second_number>',
        view_func=calculation.subtraction
    )

    # Multiply two numbers
    app.add_url_rule(
        '/mul/num/<int:first_number>/<int:second_number>',
        view_func=calculation.multiplication
    )

    # Divide two numbers
    app.add_url_rule(
        '/div/num/<int:first_number>/<int:second_number>',
        view_func=calculation.divide
    )
