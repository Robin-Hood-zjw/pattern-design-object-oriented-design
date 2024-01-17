from abc import ABC


class PriceStrategy(ABC):
    def calculate_price(self) -> float:
        pass

class Child_PriceStrategy(PriceStrategy):
    def calculate_price(self, price: float) -> float:
        return price * 0.5
    
class Adult_PriceStrategy(PriceStrategy):
    def calculate_price(self, price: float) -> float:
        return price

class Student_PriceStrategy(PriceStrategy):
    def calculate_price(self, price: float) -> float:
        return price * 0.8
    
class Holiday_PriceStrategy(PriceStrategy):
    def calculate_price(self, price: float) -> float:
        return price * 0.75


class Calculator(ABC):
    def __init__(self, strategy: PriceStrategy) -> None:
        self.strategy = strategy

    def calculate(self, price: float) -> float:
        return self.strategy.calculate_price(price)
    


if __name__ == '__main__':
    child_calculator = Calculator(Child_PriceStrategy())
    adult_calculator = Calculator(Adult_PriceStrategy())
    student_calculator = Calculator(Student_PriceStrategy())
    holiday_calculator = Calculator(Holiday_PriceStrategy())

    print(f'The original ticket price is 100, and the child ticket price is {child_calculator.calculate(100)}.')
    print(f'The original ticket price is 100, and the adult ticket price is {adult_calculator.calculate(100)}.')
    print(f'The original ticket price is 100, and the student ticket price is {student_calculator.calculate(100)}.')
    print(f'The original ticket price is 100, and the holiday ticket price is {holiday_calculator.calculate(100)}.')