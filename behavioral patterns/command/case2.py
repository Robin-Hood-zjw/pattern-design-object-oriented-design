from abc import ABC


class Drink(ABC):
    def __init__(self, name) -> None:
        self.name = name
    
    def make(self) -> None:
        print(f'{self.name} is ready!')


class Command(ABC):
    def execute(self) -> None:
        pass
    
class OrderCommand(Command):
    def __init__(self, receiver) -> None:
        self.receiver = receiver
    
    def execute(self) -> None:
        self.receiver.make()


class OrderMachine(ABC):
    def __init__(self, command) -> None:
        self.command = command
        
    def execute(self) -> None:
        self.command.execute()


if __name__ == '__main__':
    command1 = OrderCommand(Drink('Cola'))
    command2 = OrderCommand(Drink('Coffee'))
    command3 = OrderCommand(Drink('Monster Drink'))

    machine1 = OrderMachine(command1)
    machine2 = OrderMachine(command2)
    machine3 = OrderMachine(command3)

    machine1.execute()
    machine2.execute()
    machine3.execute()