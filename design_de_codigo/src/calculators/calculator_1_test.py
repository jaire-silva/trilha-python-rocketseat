from typing import Dict

from pytest import raises

from design_de_codigo.src.calculators.calculator_1 import Calculator1


class MockRequest:
    def __init__(self, body: Dict) -> None:
        self.json = body


def test_calculator_1():
    mock_request = MockRequest(body={"number": 1})
    calculator_1 = Calculator1()

    response = calculator_1.calculate(mock_request)

    # Formato esperado da resposta
    assert "data" in response
    assert "Calculator" in response["data"]
    assert response["data"]["Calculator"] == 1
    assert "result" in response["data"]

    # Assertividade da resposta
    assert response["data"]["result"] == 14.25


def test_calculator_1_with_invalid_body():
    mock_request = MockRequest(body={"something": 1})
    calculator_1 = Calculator1()

    with raises(Exception) as exc_info:
        calculator_1.calculate(mock_request)

    assert str(exc_info.value) == "Missing number in body!"