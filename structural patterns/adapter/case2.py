from abc import ABC

class Weight(ABC):
    def __init__(self, weight: float) -> None:
        self.weight = weight

    def get_weight(self) -> float:
        return self.weight

class Pound(Weight):
    def __init__(self, weight: float) -> None:
        super().__init__(weight)

    def get_weight(self) -> float:
        return super().get_weight()

class Kilogram(Weight):
    def __init__(self, weight: float) -> None:
        super().__init__(weight)

    def get_weight(self) -> float:
        return super().get_weight()


class TwoWay_Adapter(ABC):
    def __init__(self, pound=None, kilogram=None) -> None:
        if pound:
            self.pound = pound
            self.kilogram = Kilogram(round(self.pound.get_weight() / 2.205, 2))
        elif kilogram:
            self.kilogram = kilogram
            self.pound = Pound(round(self.kilogram.get_weight() * 2.205, 2))

    def get_pound(self) -> float:
        return self.pound.get_weight()

    def get_kilogram(self) -> float:
        return self.kilogram.get_weight()



if __name__ == '__main__':
    kg_weight = Kilogram(73.5)
    adapter = TwoWay_Adapter(pound=None, kilogram=kg_weight)
    print(f'The current kilogram: {adapter.get_kilogram()} kg.')
    print(f'The current pound: {adapter.get_pound()} pounds.')