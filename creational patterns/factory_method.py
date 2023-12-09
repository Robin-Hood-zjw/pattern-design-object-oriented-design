from abc import ABC

class Computer(ABC):
    def __init__(self) -> None:
        pass

class Desktop(Computer):
    _chip = None
    _weight = None
    _brand = 'Apple'

    def __init__(self) -> None:
        self._weight = 19.7
        self._chip = 'Apple M2'

class Laptop(Computer):
    _chip = None
    _weight = None
    _brand = 'Apple'

    def __init__(self) -> None:
        self._weight = 2.75
        self._chip = 'Apple M1'


class Factory(ABC):
    def manufacture(self) -> Computer:
        pass

class Desktop_Factory(ABC):
    def manufacture(self) -> Computer:
        return Desktop()
    
class Laptop_Factory(ABC):
    def manufacture(self) -> Computer:
        return Laptop()


def accept_product(factory: Factory) -> None:
    profuct = factory.manufacture()
    print("\n---------- Product Data List ----------")
    print(f"- Brand: {profuct._brand}  -----------------------")
    print(f"- Weight: {profuct._weight}  -----------------------")
    print(f"- Chip Type: {profuct._chip}  ----------------\n")



if __name__ == '__main__':
    laptop_factory = Laptop_Factory()
    desktop_factory = Desktop_Factory()

    accept_product(laptop_factory)
    # accept_product(desktop_factory)