from abc import ABC

class Mediator(ABC):
  def notify(self, message: str, sender) -> None:
    pass


class Airplane(ABC):
  def __init__(self, name: str, mediator: Mediator) -> None:
    self.name = name
    self.mediator = mediator

  def receive(self, message: str):
    print(f'{self.name} received the message. And the message: {message}')

  def send(self, message: str) -> None:
    self.mediator.notify(message, self)


class AirControl(Mediator):
  def __init__(self) -> None:
    self.airplanes = list()

  def add_airplane(self, airplane: Airplane) -> None:
    self.airplanes.append(airplane)

  def notify(self, message: str, sender) -> None:
    for airplane in self.airplanes:
      if airplane != sender:
        airplane.receive(message)
     


if __name__ == '__main__':
  system = AirControl()

  airplane1 = Airplane('Fly 1', system)
  airplane2 = Airplane('Fly 2', system)

  system.add_airplane(airplane1)
  system.add_airplane(airplane2)

  airplane1.send('Hi there.')
  airplane2.send('Hello there.')