from abc import ABC



class Builder(ABC):
    def __init__(self) -> None:
        self.frame = None
        self.tires = None
        
    def add_frame(self) -> None:
        pass
    
    def add_tires(self) -> None:
        pass
    
    def get_info(self) -> None:
        print(f'{self.frame} Frame {self.tires} Tires')

class RoadBike_Builder(Builder):
    def __init__(self) -> None:
        super().__init__()
        
    def add_frame(self) -> None:
        self.frame = 'Carbon'
    
    def add_tires(self) -> None:
        self.tires = 'Slim'
    
    def get_info(self) -> None:
        super().get_info()

class MountainBike_Builder(Builder):
    def __init__(self) -> None:
        super().__init__()

    def add_frame(self) -> None:
        self.frame = 'Aluminum'

    def add_tires(self) -> None:
        self.tires = 'Knobby'

    def get_info(self) -> None:
        super().get_info()


class BuilderDirector(ABC):
    def __init__(self, builder: Builder) -> None:
        self.builder = builder

    def build(self) -> None:
        self.builder.add_frame()
        self.builder.add_tires()

    def show_info(self) -> None:
        self.builder.get_info()



if __name__ == '__main__':
    builder1 = RoadBike_Builder()
    builder2 = MountainBike_Builder()

    director1 = BuilderDirector(builder1)
    director2 = BuilderDirector(builder2)

    director1.build()
    director2.build()

    director1.show_info()
    director2.show_info()