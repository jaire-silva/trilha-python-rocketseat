from typing import Dict


def add(elem1: int, elem2: float) -> Dict:
    response = elem1 + elem2
    return {"sum": response}


value1 = add(1, 2)
value2 = add(2.34, 12.35)
value3 = add("Hello", " World!")

print(value1)
print(value2)
print(value3)