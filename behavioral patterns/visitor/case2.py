from abc import ABC


class Item(ABC):
    def accept(self, visitor):
        pass

class Book(ABC):
    def __init__(self, price: float):
        self.price = price

    def get_price(self):
        return self.price

    def accept(self, visitor):
        visitor.visit_book(self)

class Eletronics(ABC):
    def __init__(self, price: float):
        self.price = price
    
    def get_price(self):
        return self.price
    
    def accept(self, visitor):
        visitor.visit_eletronics(self)


class Visitor(ABC):
    def __init__(self):
        self.cost = 0
    
    def visit_book(self, book: Book):
        pass
    
    def visit_eletronics(self, eletronics: Eletronics):
        pass

    def output_cost(self):
        pass

class RegularPriceVisitor(Visitor):
    def __init__(self):
        super().__init__()
    
    def visit_book(self, book: Book):
        self.cost +=  book.get_price()
    
    def visit_eletronics(self, eletronics: Eletronics):
        self.cost +=  eletronics.get_price()

    def output_cost(self):
        return self.cost
    
class DiscountPriceVisitor(Visitor):
    def __init__(self):
        super().__init__()
    
    def visit_book(self, book: Book):
        self.cost +=  book.get_price() * 0.75
    
    def visit_eletronics(self, eletronics: Eletronics):
        self.cost +=  eletronics.get_price() * 0.75

    def output_cost(self):
        return self.cost



if __name__ == '__main__':
    regular_visitor = RegularPriceVisitor()
    disount_visitor = DiscountPriceVisitor()
    items = [Book(10), Book(50), Eletronics(200)]

    for item in items:
        item.accept(regular_visitor)
        item.accept(disount_visitor)

    print(f'The regular total cost is {regular_visitor.output_cost()}')
    print(f'The discount total cost is {disount_visitor.output_cost()}')