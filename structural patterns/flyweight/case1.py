from abc import ABC

class Flyweight(ABC):
    def operate(self):
        pass

class ConcreteFlyweight(Flyweight):
    def __init__(self, state) -> None:
        self.state = state

    def operate(self) -> str:
        return f'current state: {self.state}'


class FlyweightFactory(ABC):
    def __init__(self) -> None:
        self.flyweights = dict()

    def get_flyweight(self, key: str) -> ConcreteFlyweight:
        if key not in self.flyweights:
            self.flyweights[key] = ConcreteFlyweight(key)

        return self.flyweights[key]



if __name__ == '__main__':
    factory = FlyweightFactory()
    object = factory.get_flyweight('player1')
    print(object.operate())