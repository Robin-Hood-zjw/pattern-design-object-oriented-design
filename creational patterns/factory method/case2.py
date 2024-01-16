from abc import ABC

class Block(ABC):
    def show_info(self):
        pass
    
class Circle_Block(Block):
    def show_info(self):
        print('Circle Block')
        
class Square_Block(Block):
    def show_info(self):
        print('Square Block')
        

class Factory(ABC):
    def __init__(self):
        pass
    
    def create(self):
        pass
    
class Circle_Factory(Factory):
    def __init__(self):
        self.storage = list()
    
    def create(self, num: int):
        for _ in range(num):
            block = Circle_Block()
            self.storage.append(block)
            block.show_info()
        
class Square_Factory(Factory):
    def __init__(self):
        self.storage = list()
    
    def create(self, num: int):
        for _ in range(num):
            block = Square_Block()
            self.storage.append(block)
            block.show_info()



if __name__ == '__main__':
    factory1 = Circle_Factory()
    factory2 = Square_Factory()

    factory1.create(2)
    factory2.create(3)
    