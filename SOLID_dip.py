from abc import ABC, abstractmethod

# Абстракція для абстрактної лампочки
class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

# Клас Switch тепер залежить від абстракції (Switchable), а не конкретного класу реалізації
class Switch:
    def __init__(self, device):
        self.device = device

    def operate(self):
        self.device.turn_on()

# Реалізація конкретного класу Switchable (може бути LightBulb, EnergySaverBulb, тощо)
class LightBulb(Switchable):
    def turn_on(self):
        pass

    def turn_off(self):
        pass

class EnergySaverBulb(Switchable):
    def turn_on(self):
        pass  # Реалізація для збереження енергії
