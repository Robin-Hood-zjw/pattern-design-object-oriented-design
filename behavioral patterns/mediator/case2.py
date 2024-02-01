from abc import ABC


class User(ABC):
    def __init__(self, name) -> None:
        self.name = name

    def send(self, message) -> None:
        self.mediator.send(self.name, message)

    def receive(self, message) -> None:
        print(f'{self.name} received: {message}')


class Mediator(ABC):
    def send(self, name, message) -> None:
        pass

class ChatSystem(Mediator):
    def __init__(self) -> None:
        self.users = list()

    def add_user(self, user) -> None:
        self.users.append(user)
        user.mediator = self

    def send(self, name, message) -> None:
        for user in self.users:
            if user.name != name:
                user.receive(message)


class ChatUser(User):
    pass

if __name__ == '__main__':
    system = ChatSystem()

    user1 = ChatUser('user1')
    user2 = ChatUser('user2')
    user3 = ChatUser('user3')

    system.add_user(user1)
    system.add_user(user2)
    system.add_user(user3)

    user1.send('Hi there')
    user2.send('Hey there')
    user3.send('Hello there')