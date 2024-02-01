from abc import ABC
from collections import deque


class Calculator(ABC):
    class CalculatorMemento:
        def __init__(self, result: int) -> None:
            self.result = result

        def get_result(self) -> int:
            return self.result
    
    def __init__(self) -> None:
        self.result = 0

    def get_result(self) -> int:
        return self.result
    
    def add(self, value: int) -> None:
        self.result += value

    def subtract(self, value: int) -> None:
        self.result -= value
    
    def save(self) -> CalculatorMemento:
        return self.CalculatorMemento(self.result)
    
    def restore(self, memento: CalculatorMemento) -> None:
        self.result = memento.get_result()


class CalculatorHistory(ABC):
    def __init__(self) -> None:
        self.history = deque()

    def save(self, calculator: Calculator) -> None:
        self.history.append(calculator.save())

    def undo(self, calculator: Calculator) -> None:
        if self.history:
            calculator.restore(self.history.pop())


if __name__ == '__main__':
    calculator = Calculator()
    history = CalculatorHistory()

    calculator.add(5)
    calculator.subtract(10)
    history.save(calculator)
    print(f'result: {str(calculator.get_result())}')

    calculator.subtract(8)
    history.save(calculator)
    print(f'result: {str(calculator.get_result())}')

    history.undo(calculator)
    print(f'result: {str(calculator.get_result())}')