from abc import ABC


class PriceStrategy(ABC):
    def calculate_price(self, pric: int) -> int:
        pass

class PriceStrategy1(PriceStrategy):
    def calculate_price(self, price: int) -> int:
        return int(price * 0.9)
        
class PriceStrategy2(PriceStrategy):
    def calculate_price(self, price: int) -> int:
        if price >= 300:
            return price - 40
        elif price >= 200:
            return price - 25
        elif price >= 150:
            return price - 15
        elif price >= 100:
            return price - 5
            
        return price
        

class Calculator(ABC):
    def __init__(self, strategy: PriceStrategy) -> None:
        self.strategy = strategy
        
    def calculate(self, price: int) -> int:
        return self.strategy.calculate_price(price)



if __name__ == '__main__':
    calculator1 = Calculator(PriceStrategy1())
    calculator2 = Calculator(PriceStrategy2())

    print(f'The original ticket price is 100, and the sale ticket price is {calculator1.calculate(100)} on sale for the strategt 1.')
    print(f'The original ticket price is 100, and the sale ticket price is {calculator2.calculate(100)} on sale for the strategt 2.')