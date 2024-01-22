from abc import ABC


class Drink(ABC):
    def __init__(self, name):
        self.name = name
    
    def make(self):
        print(f'{self.name} is ready!')


class Command(ABC):
    def execute(self):
        pass
    
class OrderCommand(Command):
    def __init__(self, receiver):
        self.receiver = receiver
    
    def execute(self):
        self.receiver.make()


class OrderMachine(ABC):
    def __init__(self, command):
        self.command = command
        
    def execute(self):
        self.command.execute()


if __name__ == '__main__':
    n = int(input())
    
    for _ in range(n):
        name = input()
        command = OrderCommand(Drink(name))
        machine = OrderMachine(command)
        machine.execute()