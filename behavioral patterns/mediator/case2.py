from abc import ABC


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name

    def send(self, message) -> None:
        self.mediator.send(message, self)

    def receive(self, message) -> None:
        print(f'{self.name} received: {message}')


class Mediator(ABC):
    def send(self) -> None:
        pass

class ChatSystem(Mediator):
    def __init__(self) -> None:
        self.users = list()

    def add_user(self, user) -> None:
        self.users.append(user)

    def send(self, name, message) -> None:
        for user in self.users:
            if user.name != name:
                user.receive(message)



if __name__ == '__main__':
    system = ChatSystem()
    system.add_user('user1')
    system.add_user('user2')
    system.add_user('user3')

    system.send('user1', 'Hi there')
    system.send('user2', 'Hey there')
    system.send('user3', 'Hello there')