from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def brew(self):
        pass

class BlackCoffee(Coffee):
    def brew(self) -> None:
        print('Brewing Black Coffee')

class LatteCoffee(Coffee):
    def brew(self) -> None:
        print('Brewing Latte')

class CoffeeDecorator(Coffee):
    def __init__(self, coffee) -> None:
        self.add = None
        self.coffee = coffee

    def brew(self) -> None:
        self.coffee.brew()
        print(f'Adding {self.add}')

class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee) -> None:
        super().__init__(coffee)
        self.add = 'Milk'

    def brew(self) -> None:
        super().brew()

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee) -> None:
        super().__init__(coffee)
        self.add = 'Sugar'

    def brew(self) -> None:
        super().brew()



if __name__ == '__main__':
    coffee1 = BlackCoffee()
    coffee2 = LatteCoffee()

    decorator1 = MilkDecorator(coffee1)
    decorator2 = SugarDecorator(coffee2)

    decorator1.brew()
    decorator2.brew()