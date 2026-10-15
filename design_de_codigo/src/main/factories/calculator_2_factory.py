from design_de_codigo.src.calculators.calculator_2 import Calculator2
from design_de_codigo.src.drivers.numpy_handler import NumpyHandler


def calculator_2_factory():
    driver = NumpyHandler()
    calc = Calculator2(driver)
    return calc