from abc import ABC, abstractmethod


class House(ABC):
    @abstractmethod
    def __init__(self, area):
        self.area = area
    
    @abstractmethod
    def get_area(self):
        pass

class ConcreteHouse(House):
    def __init__(self, area):
        super().__init__(area)
    
    def get_area(self):
        return self.area


class HouseAgencyProxy(ABC):
    def __init__(self):
        self.houses = list()

    def add_house(self, house):
        self.houses.append(house)

    def check(self):
        for house in self.houses:
            token = 'YES' if house.get_area() > 100 else 'NO'
            print(token)



if __name__ == '__main__':
    agency = HouseAgencyProxy()

    agency.add_house(ConcreteHouse(75))
    agency.add_house(ConcreteHouse(101))
    agency.add_house(ConcreteHouse(120))
    agency.add_house(ConcreteHouse(150))

    agency.check()