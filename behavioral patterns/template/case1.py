import sys
from abc import ABC


class Coffee(ABC):
    def __init__(self):
        self.type = None
    
    def init_coffee(self):
        print(f'Making {self.type}:')
    
    def grind_beans(self):
        print('Grinding coffee beans')
    
    def brew_coffee(self):
        print('Brewing coffee')
    
    def add_condiment(self):
        print('Adding condiments')
    
    def make_coffee(self):
        self.init_coffee()
        self.grind_beans()
        self.brew_coffee()
        self.add_condiment()

class Americano(Coffee):
    def __init__(self):
        super().__init__()
        self.type = 'American Coffee'
    
    def init_coffee(self):
        print(f'Making {self.type}:')
    
    def grind_beans(self):
        print('Grinding coffee beans')
    
    def brew_coffee(self):
        print('Brewing coffee')
    
    def add_condiment(self):
        super().add_condiment()
    
    def make_coffee(self):
        self.init_coffee()
        self.grind_beans()
        self.brew_coffee()
        self.add_condiment()

class Latte(Coffee):
    def __init__(self):
        super().__init__()
        self.type = 'Latte'
    
    def init_coffee(self):
        print(f'Making {self.type}:')
    
    def grind_beans(self):
        print('Grinding coffee beans')
    
    def brew_coffee(self):
        print('Brewing coffee')
    
    def add_condiment(self):
        print('Adding milk')
        super().add_condiment()
    
    def make_coffee(self):
        self.init_coffee()
        self.grind_beans()
        self.brew_coffee()
        self.add_condiment()


class Employee(ABC):
    def __init__(self):
        self.orders = list()

    def add_order(self, order: Coffee):
        self.orders.append(order)

    def finish_orders(self):
        for order in self.orders:
            print()
            order.make_coffee()



if __name__ == '__main__':
    employee = Employee()

    employee.add_order(Latte())
    employee.add_order(Americano())

    employee.finish_orders()