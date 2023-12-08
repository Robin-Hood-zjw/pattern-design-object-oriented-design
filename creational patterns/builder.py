from abc import ABC

class Car(ABC):
    _brand = None
    _tyres = None
    _frame = None
    _engine = None
    _suspension = None

    def __init__(self) -> None:
        self._capacity = 5

    def get_capacity(self) -> int:
        return self._capacity
    
class _product(Car):
    def __init__(self) -> None:
        self._weight = 4449

class Sedan(Car):
    def __init__(self) -> None:
        self._weight = 3848


class BMW_Builder(ABC):
    def reset(self) -> None:
        pass

    def add_brand(self) -> None:
        pass

    def add_tyres(self) -> None:
        pass

    def add_frame(self) -> None:
        pass

    def add_engine(self) -> None:
        pass

    def add_suspension(self) -> None:
        pass

    def get_product(self) -> None:
        pass


class BMW_X5_Builder(BMW_Builder):
    def reset(self) -> None:
        self._product = SUV()

    def add_brand(self) -> None:
        self._product._brand = 'BMW X5'

    def add_tyres(self) -> None:
        self._product._tyres = 'original'

    def add_frame(self) -> None:
        self._product._frame = 'unibody design'
    
    def add_engine(self) -> None:
        self._product._engine = '4.4L Turbo V8'

    def add_suspension(self) -> None:
        self._product._suspension = 'chassis and suspension'

    def get_product(self) -> Car:
        return self._product


class BMW_M5_Builder(BMW_Builder):
    def reset(self) -> None:
        self._product = Sedan()

    def add_brand(self) -> None:
        self._product._brand = 'BMW M5'

    def add_tyres(self) -> None:
        self._product._tyres = 'original'

    def add_frame(self) -> None:
        self._product._frame = 'unibody design'
    
    def add_engine(self) -> None:
        self._product._engine = '4.4-liter V-8'

    def add_suspension(self) -> None:
        self._product._suspension = 'coilover suspension'

    def get_product(self) -> Car:
        return self._product


class BMW_Car_Director:
    _car_builder = None

    def __init__(self, builder: BMW_Builder) -> None:
        self._car_builder = builder

    def switch_builder(self, builder: BMW_Builder) -> None:
        self._car_builder = builder
    
    def manufacture(self) -> Car:
        self._car_builder.reset()
        self._car_builder.add_brand()
        self._car_builder.add_tyres()
        self._car_builder.add_frame()
        self._car_builder.add_engine()
        self._car_builder.add_suspension()

    def check_quality(self) -> Car:
        product = self._car_builder.get_product()

        print("---------------- Car Info ----------------")
        print(f"Brand: {product._brand}")
        print(f"Tyre Brand: {product._tyres}")
        print(f"Frame Type: {product._frame}")
        print(f"Engine Type: {product._engine}")
        print(f"Suspension Type: {product._suspension}")
        print("------------------------------------------")
    

if __name__ == "__main__":
    director = BMW_Car_Director(BMW_X5_Builder())
    director.switch_builder(BMW_M5_Builder())
    product = director.manufacture()
    director.check_quality()