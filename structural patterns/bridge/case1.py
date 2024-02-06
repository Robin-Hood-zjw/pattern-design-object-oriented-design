from abc import ABC


class Payment(ABC):
    def process_payment(self) -> None:
        pass

class CreditCardPayment(Payment):
    def process_payment(self) -> None:
        print(f'Processing a payment with a credit card.')

class PaypalPayment(Payment):
    def process_payment(self) -> None:
        print(f'Processing a payment with a Paypal account.')


class Apple_Products(ABC):
    def __init__(self, payment: Payment) -> None:
        self.payment = payment

    def purchase(self) -> None:
        pass

class Phone(Apple_Products):
    def __init__(self, payment: Payment) -> None:
        super().__init__(payment)

    def purchase(self):
        self.payment.process_payment()
        print('The purchase of an iPhone is done.\n')

class Tablet(Apple_Products):
    def __init__(self, payment: Payment) -> None:
        super().__init__(payment)

    def purchase(self):
        self.payment.process_payment()
        print('The purchase of a tablet is done.\n')

class Laptop(Apple_Products):
    def __init__(self, payment: Payment) -> None:
        super().__init__(payment)

    def purchase(self):
        self.payment.process_payment()
        print('The purchase of a MacBook is done.\n')



if __name__ == '__main__':
    paypal = PaypalPayment()
    credit_card = CreditCardPayment()

    iPhone = Phone(credit_card)
    iPad = Tablet(credit_card)
    MacBook = Laptop(paypal)

    iPhone.purchase()
    iPad.purchase()
    MacBook.purchase()