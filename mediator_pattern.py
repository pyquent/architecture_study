from abc import ABC, abstractmethod

# Абстрактний клас Колега
class Colleague(ABC):
    def __init__(self, mediator):
        self._mediator = mediator

    @abstractmethod
    def send(self, message):
        pass

    @abstractmethod
    def receive(self, message):
        pass

# Конкретний клас Колега
class ConcreteColleagueA(Colleague):
    def send(self, message):
        self._mediator.notify(self, message)

    def receive(self, message):
        print(f"Колега A отримав повідомлення: {message}")

# Конкретний клас Колега
class ConcreteColleagueB(Colleague):
    def send(self, message):
        self._mediator.notify(self, message)

    def receive(self, message):
        print(f"Колега B отримав повідомлення: {message}")

# Абстрактний клас Посередник
class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, message):
        pass

# Конкретний клас Посередник
class ConcreteMediator(Mediator):
    def __init__(self, colleague_a, colleague_b):
        self._colleague_a = colleague_a
        self._colleague_b = colleague_b

    def notify(self, sender, message):
        if sender == self._colleague_a:
            self._colleague_b.receive(message)
        elif sender == self._colleague_b:
            self._colleague_a.receive(message)


if __name__ == "__main__":
    colleague_a = ConcreteColleagueA(None)
    colleague_b = ConcreteColleagueB(None)

    mediator = ConcreteMediator(colleague_a, colleague_b)

    colleague_a._mediator = mediator
    colleague_b._mediator = mediator

    colleague_a.send("Привіт, колего B!")
    colleague_b.send("Привіт, колего A!")



"""
Патерн "Посередник" визначає об'єкт, який координує взаємодію між об'єктами в системі.
Цей об'єкт називається посередником і дозволяє об'єктам взаємодіяти без прямих зв'язків між ними.
"""
