from abc import ABC, abstractmethod
from math import pi, sqrt


def validate_float_value(value, value_name):
    if type(value) is not float:
        raise TypeError(f"{value_name} must be float")
    elif value <= 0:
        raise ValueError(f"{value_name} must be greater zero")


# from decimal import Decimal
# I assume that in this case we can neglect the accuracy

class Figure(ABC):

    @abstractmethod
    def area(self) -> float:
        """Return figure area"""

    @abstractmethod
    def perimeter(self) -> float:
        """Return figure perimeter"""


# if you remove properties and __slots__ , you can significantly reduce the code

class Circle(Figure):
    __slots__ = ('__radius',)

    def __init__(self, radius: float = 1.0):
        self.radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius: float):
        validate_float_value(radius, "Radius")
        self.__radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def area(self):
        return pi * (self.radius ** 2)


# It might be more appropriate to use a dataclass
class Triangle(Figure):
    __slots__ = ('__sides',)

    def __init__(self, side1: float = 1.0, side2: float = 1.0, side3: float = 1.0):
        # I think that such variable names are inconvenient for the end user,
        # it is worth changing them to something more different. Example: A,B,C
        self.__sides = [side1, side2, side3]
        self.__validate_sides()

    def __get_side(self, side_index: int) -> float:
        return self.__sides[side_index]

    @property
    def side1(self) -> float:
        return self.__get_side(0)

    @property
    def side2(self) -> float:
        return self.__get_side(1)

    @property
    def side3(self) -> float:
        return self.__get_side(2)

    def __set_side(self, side_index: int, side: float):
        validate_float_value(side, f"Side{side_index}")
        self.__sides[side_index] = side

    @side1.setter
    def side1(self, side: float):
        self.__set_side(0, side)

    @side2.setter
    def side2(self, side: float):
        self.__set_side(1, side)

    @side3.setter
    def side3(self, side: float):
        self.__set_side(2, side)

    def __validate_sides(self):
        greatest_side = max(self.__sides)
        if greatest_side >= (self.perimeter() - greatest_side):
            self.__sides = []
            raise ValueError("You cannot create a degenerate triangle")

    def perimeter(self):
        return sum(self.__sides)

    def area(self):
        semiperimeter = self.perimeter() / 2
        return sqrt(
            semiperimeter *
            (semiperimeter - self.__sides[0]) *
            (semiperimeter - self.__sides[1]) *
            (semiperimeter - self.__sides[2])
        )

    def is_orthogonal(self, epsilon: float = 1e-6) -> bool:
        validate_float_value(epsilon, "Epsilon")
        # I'm using the epsilon argument because of precision issues with floats
        # https://docs.python.org/3/tutorial/floatingpoint.html
        sides_pow2_list = list(map(lambda x: x ** 2, self.__sides))
        hypotenuse = max(sides_pow2_list)
        sides_pow2_list.remove(hypotenuse)
        return hypotenuse - sum(sides_pow2_list) <= epsilon
