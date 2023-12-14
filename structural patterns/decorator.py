from abc import ABC

class Notifier(ABC):
    def send(self, message: str) -> None:
        pass

class EmailNotifier(Notifier):
    def send(self, message: str) -> None:
        print(f'Sending a notification message: {message}\n')


class Notifier_Decorator(Notifier):
    def __init__(self, notifier: Notifier) -> None:
        self.notifier = notifier

    def send(self, message: str) -> None:
        self.notifier.send(message)

class Instagram_Decorator(Notifier_Decorator):
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)

    def send(self, message: str) -> None:
        print('\nSending a Instagram message.')
        super().send(message)

class Messenager_Decorator(Notifier_Decorator):
    def __init__(self, notifier: Notifier) -> None:
        super().__init__(notifier)

    def send(self, message: str) -> None:
        print('\nSending a Messenager message.')
        super().send(message)



if __name__ == '__main__':
    test_message = 'Hello there.'
    notifier = EmailNotifier()

    instagram_notifier = Instagram_Decorator(notifier)
    messenager_notifier = Messenager_Decorator(notifier)

    instagram_notifier.send(test_message)