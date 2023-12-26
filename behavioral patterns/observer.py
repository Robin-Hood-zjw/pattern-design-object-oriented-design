from abc import ABC

class Observer(ABC):
    def update(self):
        pass

class Reader(Observer):
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

class NewsletterPublisher(Subject):
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
    publisher = NewsletterPublisher()

    user1 = Reader('Alice')
    user2 = Reader('Brooks')
    user3 = Reader('Charlie')

    publisher.register_observer(user1)
    publisher.register_observer(user2)
    publisher.register_observer(user3)
    
    publisher.publish_newsletter('New edition is on release.')

    publisher.remove_observer(user1)
    publisher.publish_newsletter('The second edition is on release.')