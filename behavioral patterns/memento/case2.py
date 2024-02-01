import sys
from abc import ABC


class App(ABC):
    def __init__(self) -> None:
        self.cur = 0
        self.prev = None

    def get_num(self) -> None:
        print(f'current number: {self.cur}')

    def increment(self) -> None:
        self.prev = self.cur
        self.cur += 1

        self.get_num()

    def decrement(self) -> None:
        self.prev = self.cur
        self.cur -= 1

        self.get_num()

    def undo(self) -> None:
        temp = self.cur
        self.cur = self.prev
        self.prev = temp

        self.get_num()

    def redo(self) -> None:
        temp = self.cur
        self.cur = self.prev
        self.prev = temp

        self.get_num()



if __name__ == '__main__':
    app = App()

    app.increment()
    app.decrement()
    app.redo()
    app.undo()