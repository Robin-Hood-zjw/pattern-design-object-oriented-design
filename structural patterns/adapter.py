from abc import ABC

class CelsiusTemperature(ABC):
    def get_celsius(self):
        pass

class FahrenheitTemperature(ABC):
    def __init__(self, temperature: int) -> None:
        self.fahrenheit_temparature = temperature

    def get_fahrenheit(self) -> int:
        return self.fahrenheit_temparature
    

class FahrenheitToCelsius_Adapter(CelsiusTemperature, FahrenheitTemperature):
    def __init__(self, temperature: int) -> None:
        super().__init__(temperature)

    def get_celsius(self) -> None:
        return (super().get_fahrenheit() - 32) * 5 / 9
    


if __name__ == '__main__':
    f = FahrenheitTemperature(100)
    adapter = FahrenheitToCelsius_Adapter(f.get_fahrenheit())

    f_temperature = f.get_fahrenheit()
    c_tempetature = adapter.get_celsius()

    print(f'\nCelsius Temperature: {c_tempetature}')
    print(f'Fahrenheit Temperature: {f_temperature}\n')