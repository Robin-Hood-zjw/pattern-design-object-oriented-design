from abc import ABC


class Currency(ABC):
    def __init__(self, amount: float) -> None:
        self.amount = amount

    def get_amount(self) -> float:
        return self.amount


class DispenseChain(ABC):
    def set_next_chain(self, next_chain) -> None:
        pass

    def dispense(self, currency: Currency) -> None:
        pass

class Dollar_50_Dispense(DispenseChain):
    def __init__(self) -> None:
        self.chain = None

    def set_next_chain(self, next_chain: DispenseChain) -> None:
        self.chain = next_chain

    def dispense(self, currency: Currency) -> None:
        if currency.get_amount() >= 50:
            notes = currency.get_amount() // 50
            remainder = currency.get_amount() % 50
            print(f'Dispensing {notes} 50 dollars.')

            if remainder > 0:
                self.chain.dispense(Currency(remainder))
        else:
            self.chain.dispense(currency)

class Dollar_20_Dispense(DispenseChain):
    def __init__(self) -> None:
        self.chain = None

    def set_next_chain(self, next_chain: DispenseChain) -> None:
        self.chain = next_chain

    def dispense(self, currency: Currency) -> None:
        if currency.get_amount() >= 20:
            notes = currency.get_amount() // 20
            remainder = currency.get_amount() % 20
            print(f'Dispensing {notes} 20 dollars.')

            if remainder > 0:
                self.chain.dispense(Currency(remainder))
        else:
            self.chain.dispense(currency)

class Dollar_10_Dispense(DispenseChain):
    def __init__(self) -> None:
        self.chain = None

    def set_next_chain(self, next_chain: DispenseChain) -> None:
        self.chain = next_chain

    def dispense(self, currency: Currency) -> None:
        if currency.get_amount() >= 10:
            notes = currency.get_amount() // 10
            remainder = currency.get_amount() % 10
            print(f'Dispensing {notes} 10 dollars.')

            if remainder > 0:
                self.chain.dispense(Currency(remainder))
        else:
            self.chain.dispense(currency)

class Dollar_5_Dispense(DispenseChain):
    def __init__(self) -> None:
        self.chain = None

    def set_next_chain(self, next_chain: DispenseChain) -> None:
        self.chain = next_chain

    def dispense(self, currency: Currency) -> None:
        if currency.get_amount() >= 5:
            notes = currency.get_amount() // 5
            remainder = currency.get_amount() % 5
            print(f'Dispensing {notes} 5 dollars.')

            if remainder > 0:
                self.chain.dispense(Currency(remainder))
        else:
            self.chain.dispense(currency)


class ATM_Dispenser(ABC):
    def __init__(self) -> None:
        self.chain1 = Dollar_50_Dispense()
        chain2 = Dollar_20_Dispense()
        chain3 = Dollar_10_Dispense()

        chain2.set_next_chain(chain3)
        self.chain1.set_next_chain(chain2)

    def dispense_cash(self, currency: Currency) -> None:
        if currency.get_amount() < 10:
            print('Amount shall be in multiples of 10.')

        self.chain1.dispense(currency)



if __name__ == '__main__':
    ATM = ATM_Dispenser()
    currency = Currency(480)
    ATM.dispense_cash(currency)