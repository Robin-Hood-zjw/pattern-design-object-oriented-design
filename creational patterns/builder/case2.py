from abc import ABC



class Builder(ABC):
    def __init__(self):
        self.frame = None
        self.tires = None
        
    def add_frame(self):
        pass
    
    def add_tires(self):
        pass
    
    def get_info(self):
        print(f'{self.frame} Frame {self.tires} Tires')

class RoadBike_Builder(Builder):
    def __init__(self):
        super().__init__()
        
    def add_frame(self):
        self.frame = 'Carbon'
    
    def add_tires(self):
        self.tires = 'Slim'
    
    def get_info(self):
        super().get_info()

class MountainBike_Builder(Builder):
    def __init__(self):
        super().__init__()

    def add_frame(self):
        self.frame = 'Aluminum'

    def add_tires(self):
        self.tires = 'Knobby'

    def get_info(self):
        super().get_info()


class BuilderDirector(ABC):
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.add_frame()
        self.builder.add_tires()

    def show_info(self):
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