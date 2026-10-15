from typing import Dict

from pytest import raises

from design_de_codigo.src.calculators.calculator_2 import Calculator2
from design_de_codigo.src.drivers.numpy_handler import NumpyHandler


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculator_2():
    mock_request = MockRequest(body={"numbers": [2.12, 4.62, 1.32]})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    response = calculator_2.calculate(mock_request)

    # Formato esperado da resposta
    assert isinstance(response, dict)
    assert "data" in response
    assert "Calculator" in response["data"]
    assert response["data"]["Calculator"] == 2
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 0.08
    assert response == {'data': {'Calculator': 2, 'result': 0.08}}


def test_calculator_2_with_invalid_body():
    mock_request = MockRequest(body={"something": 1})
    driver = NumpyHandler()
    calculator_2 = Calculator2(driver)

    with raises(Exception) as exc_info:
        calculator_2.calculate(mock_request)

    assert str(exc_info.value) == "Missing numbers in body!"