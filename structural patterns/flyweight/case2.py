import sys
from abc import ABC, abstractmethod


class ShapeFlyweight(ABC):
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.count = 1
        self.shape = None
    
    def relocate(self, x, y) -> None:
        self.x = x
        self.y = y
        self.count += 1

    @abstractmethod
    def display(self) -> None:
        token = 'drawn' if self.count < 2 else 'shared'
        print(f'{self.shape} {token} at ({self.x}, {self.y})')

class Circle(ShapeFlyweight):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.shape = 'CIRCLE'

    def relocate(self, x, y) -> None:
        super().relocate(x, y)
    
    def display(self) -> None:
        super().display()

class Rectangle(ShapeFlyweight):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.shape = 'RECTANGLE'

    def relocate(self, x, y) -> None:
        super().relocate(x, y)

    def display(self) -> None:
        super().display()

class Triangle(ShapeFlyweight):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
        self.shape = 'TRIANGLE'

    def relocate(self, x, y) -> None:
        super().relocate(x, y)

    def display(self) -> None:
        super().display()


class ShapeEditor(ABC):
    def __init__(self) -> None:
        self.record = dict()
    
    def draw(self, shape_code, x, y) -> None:
        if shape_code == 1:
            if 'circle' in self.record:
                self.record['circle'].relocate(x, y)
            else:
                self.record['circle'] = Circle(x, y)
            self.record['circle'].display()
        elif shape_code == 2:
            if 'triangle' in self.record:
                self.record['triangle'].relocate(x, y)
            else:
                self.record['triangle'] = Triangle(x, y)
            self.record['triangle'].display()
        elif shape_code == 3:
            if 'rectangle' in self.record:
                self.record['rectangle'].relocate(x, y)
            else:
                self.record['rectangle'] = Rectangle(x, y)
            self.record['rectangle'].display()



if __name__ == '__main__':
    editor = ShapeEditor()

    editor.draw(1, 1, 1)
    editor.draw(2, 5, 10)
    editor.draw(3, 11, 11)

    editor.draw(1, 11, 11)
    editor.draw(2, 20, 21)
    editor.draw(3, 55, 32)