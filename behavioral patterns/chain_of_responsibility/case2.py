from abc import ABC


class Person(ABC):
    def __init__(self, name: str, days: str) -> None:
        self.name = name
        self.days = int(days)
    
    def get_name(self) -> str:
        return self.name
        
    def get_days(self) -> int:
        return self.days


class DispenseChain(ABC):
    def set_next_chain(self, chain) -> None:
        pass
    
    def dispense(self, person: Person) -> None:
        pass
    
class Director(DispenseChain):
    def __init__(self):
        self.chain = None
        
    def set_next_chain(self, chain):
        self.chain = chain
        
    def dispense(self, person: Person) -> None:
        if person.get_days() > 10:
            print(f'{person.get_name()} Denied by Director.')
        elif person.get_days() > 7 and person.get_days() < 11:
            print(f'{person.get_name()} Approved by Director.')
        else:
            self.chain.dispense(person)

class Manager(DispenseChain):
    def __init__(self) -> None:
        self.chain = None
        
    def set_next_chain(self, chain) -> None:
        self.chain = chain
        
    def dispense(self, person: Person) -> None:
        if person.get_days() > 7:
            print(f'{person.get_name()} Denied by Manager.')
        elif person.get_days() < 8 and person.get_days() > 3:
            print(f'{person.get_name()} Approved by Manager.')
        else:
            self.chain.dispense(person)

class Supervisor(DispenseChain):
    def __init__(self) -> None:
        self.chain = None
        
    def set_next_chain(self, chain) -> None:
        self.chain = chain
        
    def dispense(self, person) -> None:
        if person.get_days() < 4:
            print(f'{person.get_name()} Approved by Supervisor.')
        else:
            print(f'{person.get_name()} Denied by Supervisor.')


class System(ABC):
    def __init__(self) -> None:
        self.c1 = Director()
        c2 = Manager()
        c3 = Supervisor()
        
        self.c1.set_next_chain(c2)
        c2.set_next_chain(c3)
        
    def dispense(self, person) -> None:
        self.c1.dispense(person)


if __name__ == '__main__':
    system = System()
    system.dispense(Person('Ada', '10'))
    system.dispense(Person('Daniel', '22'))