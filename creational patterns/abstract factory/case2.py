from abc import ABC



class Sofa(ABC):
    def show_info(self) -> None:
        pass

class ModernSofa(Sofa):
    def show_info(self) -> None:
        print('modern sofa')

class ClassicalSofa(Sofa):
    def show_info(self) -> None:
        print('classical sofa')


class Chair(ABC):
    def show_info(self) -> None:
        pass

class ModernChair(ABC):
    def show_info(self) -> None:
        print('modern chair')

class ClassicalChair(ABC):
    def show_info(self) -> None:
        print('classical chair')


class Factory(ABC):
    def create_sofa(self) -> None:
        pass

    def create_chair(self) -> None:
        pass

class ModernFactory(ABC):
    def create_sofa(self) -> Sofa:
        return ModernSofa()

    def create_chair(self) -> Chair:
        return ModernChair()

class ClassicalFactory(ABC):
    def create_sofa(self) -> Sofa:
        return ClassicalSofa()

    def create_chair(self) -> Chair:
        return ClassicalChair()



if __name__ == '__main__':
    modern_factory = ModernFactory()
    classical_factory = ClassicalFactory()

    sofa1 = modern_factory.create_sofa()
    sofa2 = classical_factory.create_sofa()

    chair1 = modern_factory.create_chair()
    chair2 = classical_factory.create_chair()

    sofa1.show_info()
    sofa2.show_info()
    chair1.show_info()
    chair2.show_info()