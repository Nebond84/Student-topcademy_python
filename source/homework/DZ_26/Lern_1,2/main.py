from rectangle import Rectangle
from circle import Circle
from  figure import Figure
from right_triangle import RightTriangle
from trapezoid import Trapezoid


rectangle = Rectangle(10.4,23.8)
circle = Circle(9)
right_triangle = RightTriangle(12.2,18.6)
trapezoid = Trapezoid(12.0,23.0,9.0)


# print(rectangle.area())

def areas(obj:Figure):
    print("===============")
    print(obj)



areas(rectangle)
areas(circle)
areas(right_triangle)
areas(trapezoid)


