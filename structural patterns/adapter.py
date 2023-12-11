from abc import ABC

class CelsiusTemperature(ABC):
    def get_temperature(self):
        pass

class FahrenheitTemperature(ABC):
    def get_temperature(self):
        pass

class Celsius(CelsiusTemperature):
    def __init__(self, temperature: int) -> None:
        self.temperature = temperature

    def get_temperature(self) -> int:
        return self.temperature
    
class Fahrenheit(FahrenheitTemperature):
    def __init__(self, temperature: int) -> None:
        self.temperature = temperature

    def get_temperature(self) -> int:
        return self.temperature
    

class Adapter(CelsiusTemperature, FahrenheitTemperature):
    def __init__(self, celsius=None, fahrenheit=None) -> None:
        if celsius:
            self.celsius = celsius
            self.fahrenheit = Fahrenheit(celsius.get_temperature() * 9 / 5 + 32)
        else:
            self.fahrenheit = fahrenheit
            self.celsius = Celsius((fahrenheit.get_temperature() - 32) * 5 / 9)

    def get_celsius_temperature(self) -> int:
        return float(self.celsius.get_temperature())
    
    def get_fahrenheit_temperature(self) -> int:
        return float(self.fahrenheit.get_temperature())

if __name__ == '__main__':
    celsius = Celsius(100)
    fahrenheit = Fahrenheit(100)

    adapter1 = Adapter(celsius=celsius)
    adapter2 = Adapter(fahrenheit=fahrenheit)

    print("\nDataset #1:")
    print(f"Celsius temperature: {adapter1.get_celsius_temperature()}")
    print(f"Fahrenheit temperature: {adapter1.get_fahrenheit_temperature()}\n")

    print("\nDataset #2:")
    print(f"Celsius temperature: {adapter2.get_celsius_temperature()}")
    print(f"Fahrenheit temperature: {adapter2.get_fahrenheit_temperature()}\n")