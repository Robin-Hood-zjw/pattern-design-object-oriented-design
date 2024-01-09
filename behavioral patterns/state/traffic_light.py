from abc import ABC

class TrafficLightState(ABC):
    def handle(self, traffic_light) -> None:
        pass

class RedLightState(TrafficLightState):
    def handle(self, traffic_light) -> None:
        print('Red Light: Stopped')
        traffic_light.state = GreenLightState()

class YellowLightState(TrafficLightState):
    def handle(self, traffic_light) -> None:
        print('Yellow Light: Stopped')
        traffic_light.state = RedLightState()

class GreenLightState(TrafficLightState):
    def handle(self, traffic_light) -> None:
        print('Green Light: Stopped')
        traffic_light.state = YellowLightState()

class TrafficLight(ABC):
    def __init__(self) -> None:
        self.state = RedLightState()

    def change(self):
        self.state.handle(self)


if __name__ == '__main__':
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.change()