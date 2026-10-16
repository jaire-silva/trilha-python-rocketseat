from typing import Dict
from typing import List

from pytest import raises

from design_de_codigo.src.calculators.calculator_3 import Calculator3
from design_de_codigo.src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
from design_de_codigo.src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


class MockDriverHandlerError(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float: pass

    def variance(self, numbers: List[float]) -> float:
        return 3


class MockDriverHandlerSuccess(DriverHandlerInterface):
    def standard_derivation(self, numbers: List[float]) -> float: pass

    def variance(self, numbers: List[float]) -> float:
        return 1000000000


def test_calculator_3_integration():
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})

    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)

    response = calculator_3.calculate(mock_request)

    # Formato esperado da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Variance" in response["data"]
    assert "Success" in response["data"]
    assert response["data"]["Calculator"] == 3

    # Assertividade da resposta
    assert response["data"]["Variance"] == 1568.16
    assert response["data"]["Success"] == True
    assert response == {'data': {'Calculator': 3, 'Variance': 1568.16, 'Success': True}}


def test_calculator_3_success():
    mock_request = MockRequest(body={"numbers": [1, 1, 1, 1, 100]})

    driver = MockDriverHandlerSuccess()
    calculator_3 = Calculator3(driver)

    response = calculator_3.calculate(mock_request)

    # Formato esperado da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert "Variance" in response["data"]
    assert "Success" in response["data"]
    assert response["data"]["Calculator"] == 3

    # Assertividade da resposta
    assert response["data"]["Variance"] == 1000000000
    assert response["data"]["Success"] == True
    assert response == {'data': {'Calculator': 3, 'Variance': 1000000000, 'Success': True}}


def test_calculator_3_with_variance_lower_than_multiplication():
    mock_request = MockRequest(body={"numbers": [1, 2, 3, 4, 5]})

    driver = MockDriverHandlerError()
    calculator_3 = Calculator3(driver)

    with raises(Exception) as exc_info:
        calculator_3.calculate(mock_request)

    assert str(exc_info.value) == "The variance is lower than the multiplication!"


def test_calculator_3_with_invalid_body():
    mock_request = MockRequest(body={"something": 1})
    driver = NumpyHandler()
    calculator_3 = Calculator3(driver)

    with raises(Exception) as exc_info:
        calculator_3.calculate(mock_request)

    assert str(exc_info.value) == "Missing numbers in body!"