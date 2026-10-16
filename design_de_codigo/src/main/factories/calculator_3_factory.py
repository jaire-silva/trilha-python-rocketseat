from design_de_codigo.src.calculators.calculator_3 import Calculator3
from design_de_codigo.src.drivers.numpy_handler import NumpyHandler


def calculator_3_factory():
    driver = NumpyHandler()
    calc = Calculator3(driver)
    return calc