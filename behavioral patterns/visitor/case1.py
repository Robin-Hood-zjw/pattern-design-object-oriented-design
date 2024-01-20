from abc import ABC

class Shape(ABC):
    def accept(self, visitor):
        pass
  
class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def get_size1(self) -> int:
        return self.radius
    
    def accept(self, visitor) -> float:
        return visitor.visit_circle(self)

class Rectangle(Shape):
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    def get_size1(self) -> int:
        return self.width
    
    def get_size2(self) -> int:
        return self.height
    
    def accept(self, visitor) -> int:
        return visitor.visit_rectangle(self)


class Visitor(ABC):
    def visit_circle(self, circle: Circle) -> None:
        pass

    def visit_rectangle(self, rectangle: Rectangle) -> None:
        pass

class AreaVisitor(Visitor):
    def visit_circle(self, circle: Circle) -> float:
        return pow(circle.get_size1(), 2) * 3.14

    def visit_rectangle(self, rectangle: Rectangle) -> int:
        return rectangle.get_size1() * rectangle.get_size2()



if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(10, 5)

    visitor1 = AreaVisitor()

    print(f'The area of this circle is {circle.accept(visitor1)}')
    print(f'The area of this rectangle is {rectangle.accept(visitor1)}')