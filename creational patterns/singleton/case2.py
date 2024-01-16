from abc import ABC


class CartSystem(ABC):
    system = None

    def __init__(self) -> None:
        self.system = dict()
        print('A new cart system is initialized.')

    def add_stuff(self, name, count) -> None:
        if self.system is None:
            self.__init__()

        self.system[name] = int(count)

    def show_info(self) -> None:
        print('\nHere are the confirmed stuff in the cart system:')
        for type, num in self.system.items():
            print(f'Type: {type} -- Count: {num}')



if __name__ == '__main__':
    cart_system = CartSystem()

    cart_system.add_stuff('book', 3)
    cart_system.add_stuff('apple', 15)
    cart_system.add_stuff('pineapple', 5)

    cart_system.show_info()