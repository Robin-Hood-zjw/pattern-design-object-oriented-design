from abc import ABC, abstractmethod


class Device(ABC):
    def __init__(self):
        self.type = None
    
    @abstractmethod
    def on(self):
        print(f'{self.type} is turned on.')
    
    @abstractmethod
    def off(self):
        print(f'{self.type} is turned off.')

class Television(Device):
    def __init__(self):
        super().__init__()
        self.type = 'Television'
    
    def on(self):
        super().on()
    
    def off(self):
        super().off()
    
class DeskLamp(Device):
    def __init__(self):
        super().__init__()
        self.type = 'Desk Lamp'
    
    def on(self):
        super().on()
    
    def off(self):
        super().off()

class AirConditioner(Device):
    def __init__(self):
        super().__init__()
        self.type = 'Air Conditioner'
    
    def on(self):
        super().on()
    
    def off(self):
        super().off()


class System(ABC):
    def __init__(self):
        self.desk_lamp = DeskLamp()
        self.television = Television()
        self.conditioner = AirConditioner()

    def on(self):
        self.desk_lamp.on()
        self.television.on()
        self.conditioner.on()

    def off(self, code):
        if code == 1:
            self.conditioner.off()
        elif code == 2:
            self.desk_lamp.off()
        elif code == 3:
            self.television.off()
        elif code == 4:
            print('All devices are off.')



if __name__ == '__main__':
    system = System()

    system.on()
    system.off(1)
    system.off(2)
    system.off(3)
    system.off(4)