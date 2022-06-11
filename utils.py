from enum import Enum
from math import sqrt
from typing import Union


class Color(Enum):
    BLUE = 1
    GREEN = 2
    RED = 3


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


def colored_items_solution(number: int) -> Enum:
    max_items = 100
    remaining = max_items - number

    if number > remaining:
        return Color.BLUE
    else:
        if number > 30:
            return Color.GREEN
        else:
            return Color.RED
