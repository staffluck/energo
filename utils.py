from math import sqrt
from typing import Union


def solve(a: float, b: float, c: float) -> Union[None, tuple, float]:
    discriminant = pow(b, 2) - (4 * a * c)

    if discriminant < 0:
        return None
    elif discriminant == 0:
        return -(b / (2 * a))
    else:
        first_solution = ((-b) + sqrt(discriminant)) / 2
        second_solition = ((-b) - sqrt(discriminant)) / 2
        return (first_solution, second_solition)
