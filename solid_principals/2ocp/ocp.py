from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    def area(self):
        return self._width * self._height


class Circle(Shape):
    def __init__(self, radius):
        self._radius = radius

    def area(self):
        return 3.14 * (self._radius ** 2)


def calculate_total_area(shapes: [Shape]):
    total = sum(shape.area() for shape in shapes)
    print(f"Total area of all shapes: {total}")


calculate_total_area([Rectangle(3, 4), Circle(5)])
