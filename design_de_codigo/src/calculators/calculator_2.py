from typing import Dict, List

from flask import request as FlaskRequest

from design_de_codigo.src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from design_de_codigo.src.errors.http_unprocessable_entity import HttpUnprocessableEntityError


class Calculator2:
    def __init__(self, driver_handler: DriverHandlerInterface):
        self.__driver_handler = driver_handler

    def calculate(self, request: FlaskRequest) -> Dict:
        body = request.json
        input_data = self.__validate_body(body)

        first_process_result = self.__first_process(input_data)
        second_process_result = self.__second_process(first_process_result)
        third_process_result = self.__third_process(second_process_result)

        calc_result = float(third_process_result)

        response = self.__format_response(calc_result)

        return response

    def __validate_body(self, body: Dict) -> List[float]:
        if "numbers" not in body:
            raise HttpUnprocessableEntityError("Missing numbers in body!")

        input_data = body["numbers"]
        return input_data

    def __first_process(self, input_data: List[float]) -> List[float]:
        first_part = [(num * 11) ** 0.95 for num in input_data]
        return first_part

    def __second_process(self, input_data: List[float]) -> float:
        first_part = self.__driver_handler.standard_derivation(input_data)
        return first_part

    def __third_process(self, number: float) -> float:
        first_part = 1 / number
        return first_part

    def __format_response(self, calc_result: float) -> Dict:
        return {
            "data": {
                "Calculator": 2,
                "result": round(calc_result, 2)
            }
        }