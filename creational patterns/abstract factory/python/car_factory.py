from abc import ABC

class Sedan(ABC):
    def on_head_light(self):
        pass


class SUV(ABC):
    def on_head_light(self):
        pass


class BMW_M5(Sedan):
    def on_head_light(self):
        print("The light of this BMW-M5 is turned on.")


class BMW_X5(SUV):
    def on_head_light(self):
        print("The light of this BMW-X5 is turned on.")


class Tesla_Model_S(Sedan):
    def on_head_light(self):
        print("The light of this Tesla-Model S is turned on.")


class Tesla_Model_Y(Sedan):
    def on_head_light(self):
        print("The light of this Tesla-Model Y is turned on.")


class CarFactory(ABC):
    def create_sedan(self) -> Sedan:
        pass

    def create_suv(self) -> SUV:
        pass


class BMW_Factory(CarFactory):
    def create_sedan(self) -> Sedan:
        return BMW_M5()
    
    def create_suv(self) -> SUV:
        return BMW_X5()
    

class Tesla_Factory(CarFactory):
    def create_sedan(self) -> Sedan:
        return Tesla_Model_S()
    
    def create_suv(self) -> SUV:
        return Tesla_Model_Y()
    

class CarDealship(ABC):
    sedan: Sedan = None
    suv: SUV = None

    def __init__(self, factory: CarFactory) -> None:
        self.sedan = factory.create_sedan()
        self.suv = factory.create_suv()

    def on_head_lights(self):
        self.sedan.on_head_light()
        self.suv.on_head_light()

if __name__ == "__main__":
    BMW_manufacturer = BMW_Factory()
    Tesla_manufacturer = Tesla_Factory()

    BMW_dealership = CarDealship(BMW_manufacturer)
    Tesla_dealership = CarDealship(Tesla_manufacturer)

    BMW_dealership.on_head_lights()
    Tesla_dealership.on_head_lights()