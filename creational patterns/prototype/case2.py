from abc import ABC



class ShapePrototype(ABC):
    def __init__(self, color, width, height):
        self.color = color
        self.width = width
        self.height = height

    def clone(self):
        pass

    def show_info(self):
        pass

class Rectangle(ShapePrototype):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

    def clone(self):
        # print('Cloned a rectangle.')
        return Rectangle(self.color, self.width, self.height)
    
    def show_info(self):
        print('Type: Rectangle')
        print(f'Color: {self.color} Width: {self.width} Height: {self.height}\n')

class Square(Rectangle):
    def __init__(self, color, width, height):
        super().__init__(color, width, height)

    def clone(self):
        # print('Cloned a square.')
        return Square(self.color, self.width, self.height)
    
    def show_info(self):
        print('Type: Square')
        super().show_info()



if __name__ == '__main__':
    rectangle1 = Rectangle('red', 10, 5)
    rectangle2 = Square('white', 40, 40)
    rectangle3 = rectangle1.clone()
    rectangle4 = rectangle2.clone()

    rectangle1.show_info()
    rectangle2.show_info()
    rectangle3.show_info()
    rectangle4.show_info()