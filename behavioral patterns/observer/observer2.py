from abc import ABC

class Observer(ABC):
    def update(self):
        pass

class Airplane(Observer):
    def __init__(self, name) -> None:
        self.name = name

    def update(self, message: str) -> None:
        print(f'Notification to {self.name}: {message}')


class Subject(ABC):
    def register_observer(self, observer: Observer) -> None:
        pass

    def remove_observer(self, observer: Observer) -> None:
        pass

    def notify_observers(self) -> None:
        pass

class Airport_Terminal(Subject):
    def __init__(self) -> None:
        self.readers = list()
        self.latest_newsletter = None

    def register_observer(self, observer: Observer) -> None:
        self.readers.append(observer)

    def remove_observer(self, observer: Observer) -> None:
        self.readers.remove(observer)

    def notify_observers(self) -> None:
        for observer in self.readers:
            observer.update(self.latest_newsletter)

    def publish_newsletter(self, newsletter: str):
        self.latest_newsletter = newsletter
        self.notify_observers()



if __name__ == '__main__':
    publisher = Airport_Terminal()

    air1 = Airplane('BA222')
    air2 = Airplane('EC452')
    air3 = Airplane('JK201')

    publisher.register_observer(air1)
    publisher.register_observer(air2)
    publisher.register_observer(air3)
    
    publisher.publish_newsletter('Alarm triggered: A storm is incoming.')

    publisher.remove_observer(air1)
    publisher.publish_newsletter('Alarm Cancelled: The weather is fine.')